OUTPUT=output.csv

.PHONY:
all: output

output :
	python Ele_Filter.py

clean :
	rm $(OUTPUT) &> /dev/null || true


