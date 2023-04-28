from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.routers import product_routes, auth_routes, order_routes
from src.jobs.write_notification import write_notification

app = FastAPI()
# uvicorn src.server:app --reload --reload-dir=src


origins = ['http://localhost:3000',
           'https://myapp.vercel.com']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)



app.include_router(product_routes.router)


app.include_router(auth_routes.router, prefix="/auth")


app.include_router(order_routes.router)


@app.post('/send_email/{email}')
def send_email(email: str, background: BackgroundTasks):
    background.add_task(write_notification,
                        email, 'Hi, how are you doing?')
    return {'OK': 'Message sent successfully'}

# Middlewares


@app.middleware('http')
async def timmingMiddleware(request: Request, next):
    print('Intercepted arrival...')

    response = await next(request)

    print('Intercepted back...')

    return response
