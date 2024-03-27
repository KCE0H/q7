from pyspark.sql.functions import col

def get_product_category_pairs(df):
    product_with_category = df.filter(col("category").isNotNull()) \
                              .select("product", "category")
    
    products_without_category = df.filter(col("category").isNull()) \
                                  .select("product")
    
    return product_with_category.union(products_without_category)