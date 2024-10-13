# declare module
# load injector
# load usecase with injector
from injector import Injector

from src.application.usecase.comment_usecase import CommentUseCase
from src.application.usecase.group_usecase import GroupFacebookUseCase
from src.application.usecase.message_usecase import MessageUseCase
from src.application.usecase.post_usecase import PostUseCase
from src.application.usecase.user_usecase import UserUseCase
from src.infrastructures.settings import config
from src.middleware.di import ApplicationModule, ApplicationTestModule

module = ApplicationModule() if config.SERVER == "PRD" else ApplicationTestModule()

injector = Injector([module])
user_usecase = injector.get(UserUseCase)
group_usecase = injector.get(GroupFacebookUseCase)
post_usecase = injector.get(PostUseCase)
message_usecase = injector.get(MessageUseCase)
comment_usecase = injector.get(CommentUseCase)
