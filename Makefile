ROOT_PATH := ${CURDIR}
SRC_PATH = ${ROOT_PATH}/src
ZIP_PATH = ${ROOT_PATH}/expense-category-populator.zip

install:
	pip install -r requirements.txt

bundle-lambda-function-zip:
	rm -rf ${ZIP_PATH}
	zip ${ZIP_PATH} requirements.txt
	cd ${SRC_PATH} && zip -r ${ZIP_PATH} .
