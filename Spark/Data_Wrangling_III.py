from pyspark.sql import SparkSession
# from pyspark.sql.functions import isnan, count, when, col, desc, udf, col, sort_array, asc, avg
# from pyspark.sql.functions import sum as Fsum
# from pyspark.sql.window import Window
# from pyspark.sql.types import IntegerType


spark = SparkSession \
    .builder \
    .appName("Spark SQL Quiz") \
    .getOrCreate()

user_log = spark.read.json("data/sparkify_log_small.json")

user_log.createOrReplaceTempView("log_table")


# Which page did user id "" (empty string) NOT visit?

user_log.printSchema()

# SELECT distinct pages for the blank user and distinc pages for all users
# Right join the results to find pages that blank visitor did not visit
spark.sql("SELECT * \
            FROM ( \
                SELECT DISTINCT page \
                FROM log_table \
                WHERE userID='') AS user_pages \
            RIGHT JOIN ( \
                SELECT DISTINCT page \
                FROM log_table) AS all_pages \
            ON user_pages.page = all_pages.page \
            WHERE user_pages.page IS NULL").show()


# How many female users do we have in the data set?

spark.sql("SELECT COUNT(DISTINCT userID) \
            FROM log_table \
            WHERE gender = 'F'").show()


# How many songs were played from the most played artist?

spark.sql("SELECT Artist, COUNT(Artist) AS plays \
        FROM log_table \
        GROUP BY Artist \
        ORDER BY plays DESC \
        LIMIT 1").show()


# How many songs do users listen to on average between visiting our home page? Please round your answer to the closest integer.

# SELECT CASE WHEN 1 > 0 THEN 1 WHEN 2 > 0 THEN 2.0 ELSE 1.2 END;
is_home = spark.sql("SELECT userID, page, ts, CASE WHEN page = 'Home' THEN 1 ELSE 0 END AS is_home FROM log_table \
            WHERE (page = 'NextSong') or (page = 'Home') \
            ")

# keep the results in a new view
is_home.createOrReplaceTempView("is_home_table")

# find the cumulative sum over the is_home column
cumulative_sum = spark.sql("SELECT *, SUM(is_home) OVER \
    (PARTITION BY userID ORDER BY ts DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS period \
    FROM is_home_table")

# keep the results in a view
cumulative_sum.createOrReplaceTempView("period_table")

# find the average count for NextSong
spark.sql("SELECT AVG(count_results) FROM \
          (SELECT COUNT(*) AS count_results FROM period_table \
GROUP BY userID, period, page HAVING page = 'NextSong') AS counts").show()
