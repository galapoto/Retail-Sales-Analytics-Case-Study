-- Example validation after importing the cleaned sale-line CSV into a sales table.
-- Grain: transaction line (InvoiceNo + StockCode may repeat legitimately).
-- Data source: UCI Online Retail. Currency: GBP. Historical 2010-2011.
SELECT COUNT(DISTINCT InvoiceNo) AS orders,
       ROUND(SUM(line_revenue_gbp),2) AS gross_sales_gbp
FROM sales;

SELECT Country, COUNT(DISTINCT InvoiceNo) AS orders,
       ROUND(SUM(line_revenue_gbp),2) AS gross_sales_gbp
FROM sales
GROUP BY Country
ORDER BY gross_sales_gbp DESC;

-- Do NOT calculate a return rate by dividing cancellation lines by sales orders:
-- line-level cancellations may be unmatched to source invoices.
