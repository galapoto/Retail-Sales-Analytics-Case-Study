# Google Data Analytics certificate originally included R Programming (2025 syllabus).
# Independent optional R verification, using exported processed CSV from Python.
# Usage: Rscript analysis/retail_case_study.R data/raw/online_retail.csv
args <- commandArgs(trailingOnly=TRUE)
if (length(args) < 1) stop('Pass raw UCI CSV file path')
data <- read.csv(args[1], stringsAsFactors=FALSE, check.names=FALSE)
needed <- c('InvoiceNo','StockCode','Quantity','UnitPrice','InvoiceDate','Country')
if (!all(needed %in% names(data))) stop('UCI columns missing')
cat('Raw rows:', nrow(data), '\n')
cat('Exact duplicate rows:', sum(duplicated(data)), '\n')
clean <- unique(data)
clean$Quantity <- as.numeric(clean$Quantity)
clean$UnitPrice <- as.numeric(clean$UnitPrice)
sale <- clean[!grepl('^C', toupper(clean$InvoiceNo)) & clean$Quantity>0 & clean$UnitPrice>0 &
              !is.na(clean$InvoiceDate) & !is.na(clean$Quantity) & !is.na(clean$UnitPrice),]
sale$gross_revenue_gbp <- sale$Quantity * sale$UnitPrice
cat('Distinct sale invoices:', length(unique(sale$InvoiceNo)), '\n')
cat('Gross sales GBP:', round(sum(sale$gross_revenue_gbp),2), '\n')
by_country <- aggregate(gross_revenue_gbp~Country,sale,sum)
print(head(by_country[order(-by_country$gross_revenue_gbp),],10))
