# -*- coding: utf-8 -*-
"""
@Author:    mzhang
@File:      test_mainpage.py
@Date:      2021/09/25
@Desc:
"""
from pages.basepage import *

import pytest
import time

def test_validate_title():
	mp = mainpage()
	mp.open_url("https://crypto.com/exchange")
	mp.category_navigate("USDC")
	mp.trade_navigate("CRO/USDC")
	time.sleep(5)
	title = mp.get_title()
	mp.close()
	assert "CROUSDC" in title


if __name__ == '__main__':
		pytest.main(['-sv', 'test_mainpage.py'])
