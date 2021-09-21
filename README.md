
# Statement
Any financial analyst (and sometimes business analyst) has to process financial statements from time to time. 
For private companies this can be a pain – most of the information is often in PDF and has to be extracted with either proprietary software (for which you need budget) or by hands (which is cumbersome). 

This is a script which converts PDF statements into Excels right on your machine with 0 costs.

## Deps

The script depends on the `pytesseract, pandas, sklearn, numpy`

## Docs

*`(class) Statement (image, x, y)`*

 - image: PIL image obj, default = None, A Python Imaging Library object which contains scan of the statement.
 - x : int, default = None, Number of rows in the statement.
 - y: int, default = None, Number of columns in the statement.

This has to be inputed by hand. I experimented with automatic clustering but for my purposes (small statements) the qualty-automation trade-off has been in favour of the more manual solution. 

`(function) Statement.recognise ()`

The function recognises table on the image and creates a NumPy matrix with the statement inside. The function uses Agglomerative Clustering with single linkage to cluster columns and rows in the tightest groups. **I advise not to change that as most of the other algorithms (mainly similar to K-Means) build clusters around cluster means which is not a good option given than py-tesseract returns top left coordinate of any word rather than its center point.**  

**return: none**

 
`(function) Statement.store (location = 'my_excel_file.xlsx')`
 - location : str, default = 'my_excel_file.xlsx', choose where to create Excel file with the statement copy.

**return: none**
 
