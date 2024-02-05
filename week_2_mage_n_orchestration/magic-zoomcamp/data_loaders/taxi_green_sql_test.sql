-- Docs: https://docs.mage.ai/guides/sql-blocks
select a."vendor_id" from mage.green_taxi as a group by a."vendor_id" 