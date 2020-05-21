Logger日志分级小工具



基础使用 默认输出到控制台 日志等级默认DEBUG

```python
import logger
logger.debug("debug msg")
logger.info("info msg")

```

保存到文件  logfile  

```python
from logger import InitLogConfig
import logger

InitLogConfig(dev=False)

logger.debug("DEBUG")
logger.info("INFO")
logger.error("INFO")
logger.warning("INFO")
logger.fatal("INFO")

```

限制显示日志等级

```python
from logger import InitLogConfig
import logger
import logging

InitLogConfig(loglevel=logging.INFO)

logger.debug("DEBUG")
logger.info("INFO")
logger.error("INFO")
logger.warning("INFO")
logger.fatal("INFO")
```

具体介绍:

[https://zhuanlan.zhihu.com/p/142546867](知乎)

