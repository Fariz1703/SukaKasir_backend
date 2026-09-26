from database.database import Base
import models


print("Tables:")

for table in Base.metadata.tables:
    print("-", table)