from fastapi import FastAPI
from butler.models import models
from butler.database import database
from butler.routers import user, authentication, bill, client_type, client, reduction, reservation, role, space_state, space_type, space, to_bill

app = FastAPI()
 
models.database.Base.metadata.create_all(database.engine)

app.include_router(authentication.router)
app.include_router(bill.router)
app.include_router(client_type.router)
app.include_router(client.router)
app.include_router(reduction.router)
app.include_router(reservation.router)
app.include_router(role.router)
app.include_router(space_state.router)
app.include_router(space_type.router)
app.include_router(space.router)
app.include_router(to_bill.router)
app.include_router(user.router)




