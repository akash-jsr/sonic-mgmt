import allure
import logging

logger = logging.getLogger()

CONFIGURE_BANNER_CMD = "config banner "
SHOW_BANNER_CMD = "show banner"
NO_BANNER = "no banner "
PASSWORD = "admin"
FAILED = "failed"
DEF_STATE = "disabled"
NEW_STATE = "enabled"
DEF_LOGIN_MSG = "Debian GNU/Linux 11"
DEF_MOTD_MSG = "This is temporary default MOTD"
DEF_LOGOUT_MSG = ""
NEW_LOGIN_MSG = "Welcome to SONIC CLI"
NEW_MOTD_MSG = "This is SONIC"
NEW_LOGOUT_MSG = "Good Bye!"
SUDO_STR = "sudo "
LOGIN_STR = "login "
MOTD_STR = "motd "
LOGOUT_STR = "logout "
STATE_STR = "state "


def test_system_banner_message_login(engines):
    """
    :param dut: object for device under test
    :return: None
    Verify the set command for system login banner message which comes with the login prompt
    Test flow:
        1. Configure 'login' message:set
        2. Enable the banner feature
        3. Check login banner config by show
        4. Logout and check the login message
        5. Disable back the banner feature
    """
    duthost = engines.dut

    try:
        with allure.step('Enable banner feature'):
            cmd_to_execute = SUDO_STR + CONFIGURE_BANNER_CMD + STATE_STR + NEW_STATE
            output = duthost.run_cmd(cmd_to_execute)
            assert not (output and FAILED not in output), "Failed to execute cmd:" + cmd_to_execute

        with allure.step('Run configure login message command and apply config'):
            cmd_to_execute = SUDO_STR + CONFIGURE_BANNER_CMD + LOGIN_STR + "'" + NEW_LOGIN_MSG + "'"
            output = duthost.run_cmd(cmd_to_execute)
            assert not (output and FAILED not in output), "Failed to execute cmd:" + cmd_to_execute

        with allure.step('Check banner login message via show command'):
            output = duthost.run_cmd(SHOW_BANNER_CMD)
            assert (output and NEW_LOGIN_MSG in output), "Login message is not configured"

        """
        with allure.step('Run ssh to the device command and check login message'):
            hostname = duthost.run_cmd("hostname")
            output = duthost.run_cmd("ssh admin@" + hostname)
            if "sure" in output:
                duthost.run_cmd("yes")
            assert (output and NEW_LOGIN_MSG in output), "Login message is not configured in functionality"
            logger.info("Login banner messages tests completed")
        """

    finally:
        with allure.step('Unset the login message to make it default'):
            cmd_to_execute = SUDO_STR + CONFIGURE_BANNER_CMD + LOGIN_STR + "'" + DEF_LOGIN_MSG + "'"
            output = duthost.run_cmd(cmd_to_execute)
            assert not (output and FAILED not in output), "Failed to execute cmd:" + cmd_to_execute

        with allure.step('Disable banner feature'):
            cmd_to_execute = SUDO_STR + CONFIGURE_BANNER_CMD + STATE_STR + DEF_STATE
            output = duthost.run_cmd(cmd_to_execute)
            assert not (output and FAILED not in output), "Failed to execute cmd:" + cmd_to_execute


def test_system_banner_message_motd(engines):
    """
    :param dut: object for device under test
    :return: None
    Verify the set command for system message of the day banner message which comes after the login prompt
    Test flow:
        1. Enable the banner feature
        2. Configure 'motd' message:set
        3. Check motd banner config by show
        4. Login and check the motd message
        5. Disable back the banner feature
    """

    duthost = engines.dut
    with open("/root/mars/workspace/sonic-mgmt/ansible/roles/sonic-common/files/etc/motd", "r") as file:
        DEF_MOTD_MSG = file.read()
    logger.info("Akash:\n".format(DEF_MOTD_MSG))

    try:
        with allure.step('Enable banner feature'):
            cmd_to_execute = SUDO_STR + CONFIGURE_BANNER_CMD + STATE_STR + NEW_STATE
            output = duthost.run_cmd(cmd_to_execute)
            assert not (output and FAILED not in output), "Failed to execute cmd:" + cmd_to_execute

        with allure.step('Run configure motd message command and apply config'):
            cmd_to_execute = SUDO_STR + CONFIGURE_BANNER_CMD + MOTD_STR + "'" + NEW_MOTD_MSG + "'"
            output = duthost.run_cmd(cmd_to_execute)
            assert not (output and FAILED not in output), "Failed to execute cmd:" + cmd_to_execute

        with allure.step('Check MOTD banner message via show command'):
            output = duthost.run_cmd(SHOW_BANNER_CMD)
            assert (output and NEW_MOTD_MSG in output), "MOTD message is not configured"

        """
        with allure.step('Run ssh to the device command and check MOTD message'):
            hostname = duthost.run_cmd("hostname")
            output = duthost.run_cmd("ssh admin@" + hostname)
            if "sure" in output:
                duthost.run_cmd("yes")
            output = duthost.run_cmd(PASSWORD)
            assert (output and NEW_MOTD_MSG in output), "MOTD message is not configured"
            logger.info("MOTD banner messages tests completed")
        """

    finally:
        with allure.step('Unset the MOTD message to make it default'):
            cmd_to_execute = SUDO_STR + CONFIGURE_BANNER_CMD + MOTD_STR + "'" + DEF_MOTD_MSG + "'"
            output = duthost.run_cmd(cmd_to_execute)

        with allure.step('Disable banner feature'):
            cmd_to_execute = SUDO_STR + CONFIGURE_BANNER_CMD + STATE_STR + DEF_STATE
            output = duthost.run_cmd(cmd_to_execute)
            assert not (output and FAILED not in output), "Failed to execute cmd:" + cmd_to_execute


def test_system_banner_message_logout(engines):
    """
    :param dut: object for device under test
    :return: None
    Verify the set command for system logout banner message which comes after logging out
    Test flow:
        1. Enable the banner feature
        2. Configure 'logout' message:set
        3. Check logout banner config by show
        4. Logout and check the logout message
        5. Disable back the banner feature
    """

    duthost = engines.dut

    try:
        with allure.step('Enable banner feature'):
            cmd_to_execute = SUDO_STR + CONFIGURE_BANNER_CMD + STATE_STR + NEW_STATE
            logger.info("Akash")
            output = duthost.run_cmd(cmd_to_execute)
            assert not (output and FAILED not in output), "Failed to execute cmd:" + cmd_to_execute

        with allure.step('Run configure login message command and apply config'):
            cmd_to_execute = SUDO_STR + CONFIGURE_BANNER_CMD + LOGOUT_STR + "'" + NEW_LOGOUT_MSG + "'"
            output = duthost.run_cmd(cmd_to_execute)
            assert not (output and FAILED not in output), "Failed to execute cmd:" + cmd_to_execute

        with allure.step('Check banner logout message via show command'):
            output = duthost.run_cmd(SHOW_BANNER_CMD)
            assert (output and NEW_LOGOUT_MSG in output), "Logout message is not configured"

        """
        with allure.step('Logout and check logout message'):
            hostname = duthost.run_cmd("hostname")
            output = duthost.run_cmd("exit")
            assert (output and NEW_LOGOUT_MSG in output), "Logout message is not configured in functionality"
            logger.info("Logout banner messages tests completed")
        """

    finally:
        with allure.step('Unset the logout message to make it default'):
            cmd_to_execute = SUDO_STR + CONFIGURE_BANNER_CMD + LOGOUT_STR + "'" + DEF_LOGOUT_MSG + "'"
            output = duthost.run_cmd(cmd_to_execute)
            assert not (output and FAILED not in output), "Failed to execute cmd:" + cmd_to_execute

        with allure.step('Disable banner feature'):
            cmd_to_execute = SUDO_STR + CONFIGURE_BANNER_CMD + STATE_STR + DEF_STATE
            output = duthost.run_cmd(cmd_to_execute)
            assert not (output and FAILED not in output), "Failed to execute cmd:" + cmd_to_execute

