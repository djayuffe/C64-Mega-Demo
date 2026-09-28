# Copyright (C) 2026 Ulf Bertilsson
# SPDX-License-Identifier: GPL-3.0-or-later

.DEFAULT_GOAL := all
.PHONY: all audit build verify clean

ACME ?= acme
PYTHON ?= python3
SHA256SUM ?= shasum -a 256
PROGRAM := build/c64-mega-demo-3sid.prg

all: build

audit:
	$(PYTHON) tools/static_audit.py

build: audit
	mkdir -p build
	cd src && $(ACME) --strict-segments -f cbm -o ../$(PROGRAM) subway.s
	@echo "Built $(PROGRAM)"

verify: build
	$(SHA256SUM) -c SHA256SUMS.txt

clean:
	rm -rf build
