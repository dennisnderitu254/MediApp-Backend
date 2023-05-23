import database as db

db = db.Database("medicentral")
db.setLocalhost("localhost")
db.setUsername("root")
db.setPassword("root1234")
db.createDatabase()

db.setTableName("customers")
db.createTable()
