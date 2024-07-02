.PHONY: all readme clean


_TARGET_RESOURCE = schedules
_TARGET_CLSNAME = Schedule

_RESOURCE = orders
_CLSNAME = Order



all:
	@echo $(_README)


readme:
	@sed "s/$(_RESOURCE)/$(_TARGET_RESOURCE)/g" $(PWD)/README.md > TBD_README
	@sed "s/$(_CLSNAME)/$(_TARGET_CLSNAME)/g" TBD_README > $(PWD)/README_$(_RESOURCE).md


clean:
	rm -f TBD_*
	rm -r __py*
	chmod +xrw ./.idea && rm -r ./.idea
	rm -f clean
