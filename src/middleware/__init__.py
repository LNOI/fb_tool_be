# declare module
# load injector
# load usecase with injector
from injector import  Injector

from src.application.usecase.user_usecase import UserUseCase
from src.infrastructures.settings import config
from src.middleware.di import ApplicationModule, ApplicationTestModule

module = (
    ApplicationModule() if config.SERVER == "PRD" else ApplicationTestModule()
)

injector = Injector([module])
user_usecase = injector.get(UserUseCase)