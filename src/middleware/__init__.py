from injector import Injector

from src.application.usecase.accounts_usecase import AccountsUseCase
from src.application.usecase.comment_usecase import CommentUseCase
from src.application.usecase.group_usecase import GroupFacebookUseCase
from src.application.usecase.message_usecase import MessageUseCase
from src.application.usecase.post_usecase import PostUseCase
from src.application.usecase.sessions_usecase import SessionsUseCase
from src.application.usecase.users_usecase import UsersUseCase
from src.application.usecase.history_scrape_usecase import HistoryScrapeUseCase
from src.infrastructures.settings import config
from src.middleware.di import ApplicationModule, ApplicationTestModule

module = ApplicationModule() if config.SERVER == "PRD" else ApplicationTestModule()

injector = Injector([module])
group_usecase = injector.get(GroupFacebookUseCase)
post_usecase = injector.get(PostUseCase)
message_usecase = injector.get(MessageUseCase)
comment_usecase = injector.get(CommentUseCase)
hc_usecase = injector.get(HistoryScrapeUseCase)
users_usecase = injector.get(UsersUseCase)
accounts_usecase = injector.get(AccountsUseCase)
sessions_usecase = injector.get(SessionsUseCase)
