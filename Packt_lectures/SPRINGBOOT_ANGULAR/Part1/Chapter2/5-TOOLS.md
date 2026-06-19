# 31

## [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

- create a file with eiter the .http or .rest extensio

```bash
jmena01@m077-2281091:~/CONSULTANT/TESTRESTClient$ cat exmaple.rest
GET https://test.com/users/1 HTTP/1.1
###
GET https://test.com /blogs/1 HTTP/1.1
###
POST https://test.com/rate HTTP/1.1
content-type: application/json
{
    "name": "sample",
    "rate": 5:
}
```

## Run a request

- Above each request in the editor there is a **Send Request** link
  - click on it to run the request
- or select the Request / right click / Send Request (menu). It is the same as the following keys combination: **CTRL + ALT + R**
- \#\#\# lines are mandatory to end a request otherwise the followin text is seen ad Body in case of a POST Request

## Angular dev tools

- Is is also a [Firefox Extension](https://addons.mozilla.org/en-US/firefox/addon/angular-devtools/)
  - perhaphs it is not so well developped as the Chrome extension
