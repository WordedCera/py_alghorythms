import pymssql

class Repository:

    def getFilteredProducts(self, fitstLetters):
        connection = pymssql.connect(
        server="********",
        database="****",
        user="**",
        password="******"
        )

        sql = f"""
            select ProductID, Name, ProductNumber, ListPrice 
            from Production.Product
            where Name like '{fitstLetters}%'
        """

        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        connection.close()

        products = []
        # print(results)
        # f = open("data/expensive.csv","w",encoding="UTF-8")
        # f.write('id,name,code,price\n')
        for product in results:
            id = product[0]
            name = product[1]
            code = product[2]
            price = float(product[3])
            products.append(
                {
                    "id":id,
                    "name":name,
                    "code":code,
                    "price":price
                }
            )
        
        return products
if __name__ == "__main__":
    repository = Repository()
    print(repository.getFilteredProducts(""))
