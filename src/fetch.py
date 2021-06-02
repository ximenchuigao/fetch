from fund_sync.request_builder.fund_industry_builder import FundIndustryReq
from fund_sync.funds_manager_task import FundsManagerTask
from fund_sync.funds_type_task import FundsTypeTask
from fund_sync.funds_benefit_task import FundsBenefitTask
from fund_sync.funds_industry_task import FundsIndustryTask
from common.init_db import InitDb
from fund_sync.funds_params_task import FundsParamsTask


if __name__ == "__main__":
    InitDb().start()
    FundsTypeTask.do()
    FundsManagerTask.do()
    FundsBenefitTask.do()
    FundsIndustryTask.do()
    # FundsParamsTask.do();
