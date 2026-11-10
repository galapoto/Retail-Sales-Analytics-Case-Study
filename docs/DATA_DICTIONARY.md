# Data dictionary and business rules

Original source: [UCI Online Retail (Daqing Chen, 2015)](https://archive.ics.uci.edu/dataset/352/online+retail), CC BY 4.0. This is a **historical UK non-store retailer**, not data from HOK-Elanto or a Finnish grocery business.

| Field | Meaning | Validation |
|---|---|---|
| InvoiceNo | Invoice ID; C prefix denotes cancellation | Not null; preserved as string |
| StockCode | Product reference | Not null; preserved as string |
| Description | Item description | Missing values allowed but flagged |
| Quantity | Units; negative on cancellation records | Numeric |
| InvoiceDate | Invoice timestamp | Parseable date |
| UnitPrice | Price in GBP per unit | Numeric and nonnegative |
| CustomerID | Pseudonymous customer ID | Optional; unknown IDs do not imply one customer |
| Country | Customer billing country | Nonblank |

## Explicit metrics policy

- **Gross sales** = sum(Quantity × UnitPrice) for positive-quantity, positive-price non-cancelled invoice lines after removing exact duplicates. This is neither net revenue nor operating profit.
- **Cancellation line value** = sum(abs(Quantity) × UnitPrice) for cancellation invoices with negative quantity and positive unit price. It is **reported separately**; cancellations are not automatically matched with earlier sales.
- **Orders** = distinct non-cancelled invoice identifiers among valid sale lines.
- **Average order value** = gross sales divided by valid distinct orders.
- **Identified customers** = distinct nonmissing CustomerID; unknown customers excluded.
- **Monthly sales** = valid positive sale-line revenue by invoice month.
- **Country and product breakdowns** = valid positive sale-line revenue by each grouping.

The UCI data contains no cost of goods sold, margin, marketing spend, intervention assignment or store footfall. Profit and causal marketing uplift cannot be inferred.
