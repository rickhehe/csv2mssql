import os
from sqlalchemy.orm import Session
from base import Base, engine

# import all tables required from tables module
from tables import DimHolidayNZ, DimDept

from raw import df_x, df_d
print(df_x)
print(df_d)

#for table in Base.metadata.tables:
#    print(table)

if __name__ == '__main__':

    list_of_objects_x = [
        DimHolidayNZ(id=x.id, name=x.name, dateKey=x.dateKey)
        for x
        in df_x.itertuples(index=None)
    ]

    list_of_objects_d = [
        DimDept(id=x.ID, name=x.Name, groupName=x.GroupName)
        for x
        in df_d.itertuples(index=None)
    ]


    Base.metadata.create_all(engine)

    session = Session(engine)

    session.bulk_save_objects(list_of_objects_x)
    session.bulk_save_objects(list_of_objects_d)

    session.commit()
