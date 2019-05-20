# Inserting on conflict do nothing

INSERT INTO customer_address (customer_id, customer_street, customer_city, customer_state)
VALUES
  (
  432, '923 Knox Street', 'Albany', 'NY')
  )
ON CONFLICT (customer_id)
DO NOTHING



# Inserting on conflict update

INSERT INTO customer_address (customer_id, customer_street)
VALUES
  (
    432. '923 KNOX Street, Suite 1'
  )
ON CONFLICT (customer_id)
DO UPDATE
    SET customer_street = EXCLUDED.customer_street;:
