import pytest

from CM_testcase.Authentication.login import Login
from CM_testcase.CM_pages.Action import Actiontracker
from CM_testcase.CM_pages.Configure.action_stage import Actionstage
from CM_testcase.CM_pages.Configure.asset import Assettype
from CM_testcase.CM_pages.Configure.group import Group
from CM_testcase.CM_pages.DEFINE_FORMS.Forms import Forms
from CM_testcase.CM_pages.ER_page import Establish_realation
from CM_testcase.CM_pages.Home import Homepage
from CM_testcase.CM_pages.REPORTS.Checklistreport import ChecklistReport
from CM_testcase.CM_pages.REPORTS.aging import AgingReport
from CM_testcase.CM_pages.REPORTS.default import DefaultReport
from CM_testcase.CM_pages.REPORTS.formfilledreports import FormfilledReport
from CM_testcase.CM_pages.Assign import Assign
from CM_testcase.CM_pages.calendar import Calendar


@pytest.mark.usefixtures("setup")
class Test_All:

    @pytest.mark.login
    def test_a_login(self):
        self.login = Login(self.driver)
        self.login.login()

    @pytest.mark.homepage
    def test_b_home(self):
        self.login = Login(self.driver)
        self.login.login()

        self.home = Homepage(self.driver)
        self.home.home_page()

    @pytest.mark.forms
    def test_c_forms(self):
        self.login = Login(self.driver)
        self.login.login()

        self.forms = Forms(self.driver)
        self.forms.form_page()

    @pytest.mark.checklistreport
    def test_d_checklistreport(self):
        self.login = Login(self.driver)
        self.login.login()

        self.checklistreport = ChecklistReport(self.driver)
        self.checklistreport.checklistreport_page()

    @pytest.mark.formfilledreports
    def test_e_formfilledreports(self):
        self.login = Login(self.driver)
        self.login.login()

        self.formfilledreports = FormfilledReport(self.driver)
        self.formfilledreports.formfilledreport_page()

    @pytest.mark.defaultreport
    def test_f_defaultreport(self):
        self.login = Login(self.driver)
        self.login.login()

        self.defaultreport = DefaultReport(self.driver)
        self.defaultreport.defaultreport_page()

    @pytest.mark.agingreport
    def test_g_agingreport(self):
        self.login = Login(self.driver)
        self.login.login()
        self.agingreport = AgingReport(self.driver)
        self.agingreport.agingreport_page()

    @pytest.mark.assign
    def test_h_assign(self):
        self.login = Login(self.driver)
        self.login.login()

        self.assign = Assign(self.driver)
        self.assign.assign_page()

    @pytest.mark.actiontracker
    def test_i_actiontracker(self):
        self.login = Login(self.driver)
        self.login.login()

        self.actiontracker = Actiontracker(self.driver)
        self.actiontracker.action_page()

    @pytest.mark.establishrealation
    def test_j_establishrealation(self):
        self.login = Login(self.driver)
        self.login.login()

        self.establishrealation = Establish_realation(self.driver)
        self.establishrealation.er_page()

    @pytest.mark.calendar
    def test_k_calendar(self):
        self.login = Login(self.driver)
        self.login.login()

        self.calendar =Calendar (self.driver)
        self.calendar.calendar_page()

    @pytest.mark.actionstage
    def test_l_actionstage(self):
        self.login = Login(self.driver)
        self.login.login()

        self.actionstage = Actionstage(self.driver)
        self.actionstage.actionstage_page()

    @pytest.mark.assettype
    def test_m_assettype(self):
            self.login = Login(self.driver)
            self.login.login()

            self.assettypes = Assettype(self.driver)
            self.assettypes.assettype_page()

    @pytest.mark.group
    def test_n_group(self):
        self.login = Login(self.driver)
        self.login.login()

        self.groups = Group(self.driver)
        self.groups.group_page()


if __name__ == "__main__":
    pytest.main()
