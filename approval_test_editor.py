from logger import log
#used to create a txt file used for approval testing


log.enable_save_to_txt("approval_test_valid.txt")

log.info("testing info clean")
log.error("testing error clean")
log.warning("testing warning clean")
log.success("testing success clean")

