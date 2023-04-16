faas build stack.yml \
    --build-arg "HTTP_PROXY=http://172.17.0.1:7890/" \
    --build-arg "HTTPS_PROXY=http://172.17.0.1:7890/" \
    --build-arg "http_proxy=http://172.17.0.1:7890/" \
    --build-arg "https_proxy=http://172.17.0.1:7890/" \
    --build-arg "NO_PROXY=*"
faas deploy stack.yml