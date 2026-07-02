from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    wait_random
)


retry_config = retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(min=1, max=10)
         + wait_random(0, 1),
    reraise=True
)