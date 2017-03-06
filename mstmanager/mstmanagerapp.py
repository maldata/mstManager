import sys
import os.path
import logging
import logging.config
import logging.handlers
import traceback

import mstmanager.controllers.main
import mstmanager.db.engine


def exception_hook(etype, value, tb):
    logging.critical("Uncaught exception\n%s", ''.join(traceback.format_exception(etype, value, tb)))
    logging.info("Terminating MSTManager")

    # attempt to deinitialize all engines and shutdown gracefully
    # if it doesn't work, take the ugly approach
    try:
        # shared.deinitialize()
        sys.exit(1)
    except Exception as e:
        logging.exception("Exception occurred during deinitialization, terminating process")
        os._exit(os.EX_SOFTWARE)


def main():
    # app = QApplication(sys.argv)

    # get directory that stores all external files
    # data_dir = directory.get_data_directory()

    # setup logging with default configuration
    # logger_config.setup_logging(file_directory=data_dir)
    logger = logging.getLogger(__name__)

    logger.info("Starting MST Manager")

    # use custom hook for handling uncaught exceptions
    sys.excepthook = exception_hook

    # TODO: Parse the command line arguments to figure out if we're running a CLI or a Tk app
    db = mstmanager.db.engine.DbEngine()
    db.initialize()
    
    main_controller = mstmanager.controllers.main.MainController(db)
    main_controller.initialize()
    main_controller.run()

    # parse the configuration file
    # config_dict = config.load_config(data_dir)

    # reinitialize logging with logging level defined in configuration
    # logger_config.setup_logging(file_directory=data_dir, file_logging_level=config_dict["min_logging_level"])

    # set font
    # font_file = os.path.join(directory.get_resources_directory(), config_dict["font_filename"])
    # if os.path.isfile(font_file):
    #     font_id = QFontDatabase.addApplicationFont(font_file)
    #     if font_id != -1:
    #         font = QFont(config_dict["font_name"])
    #         app.setFont(font)
    #     else:
    #         logger.warning("Failed to add font")
    # else:
    #     logger.warning("Font file not found at " + font_file)



    # register base controller so screens can connect to slots and signals in derived classes
    # qmlRegisterType(BaseController, 'BaseController', 1, 0, 'BaseController')
    #
    # engine = QQmlApplicationEngine()
    #
    # main_controller = MainController(config_dict)
    #
    # context = engine.rootContext()
    # context.setContextProperty("main", main_controller)
    #
    # engine.load("expresslocker/qml/main.qml")
    #
    # main_controller.startup()
    #
    # app.exec_()

    main_controller.deinitialize()
    db.deinitialize()
    
    sys.exit()


if __name__ == '__main__':
    main()
