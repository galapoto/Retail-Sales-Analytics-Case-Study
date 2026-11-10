# Power BI implementation blueprint

Use processed monthly_sales.csv, country_sales.csv and top20_products.csv in Power BI Desktop for a rapid read-only reporting prototype. These outputs are separately aggregated; do **not** form a fact table by joining aggregates to each other.

For more flexible filtering and drill-down, import the clean sales-transaction lines and define separate **Date**, **Product**, **Country** dimension tables. Avoid many-to-many joins and validate filter direction.

Suggested measures for a valid sale-line fact table named Sales:

```DAX
Gross Sales GBP = SUM(Sales[line_revenue_gbp])
Orders = DISTINCTCOUNT(Sales[InvoiceNo])
Average Order Value GBP = DIVIDE([Gross Sales GBP], [Orders])
```

Suggested pages:
- Overview: gross sales, order count, average order value, monthly sales trend.
- Markets: country sales ranking and share (historical, not representative of Finland).
- Data quality: duplicate/missing record counts, defined cancellation value and data limitations.

**What is delivered:** Power BI metric design guidance. **What is not delivered:** a native .pbix file, deployed Power BI Service workspace or published interactive report. Do not infer a validated net-return ratio until the original invoice matching approach is documented.
