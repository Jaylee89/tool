from statistics import mode
import requests
import base64


headers_with_book118 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Host": "view-cache.book118.com",
    "Cookie": "CLIENT_SYS_UN_ID=wKh2CmBQsAVaFErUIQvBAg==; s_v=cdh%3D%3E27a30245%7C%7C%7Cvid%3D%3E1615900678150153421%7C%7C%7Cfsts%3D%3E1615900678%7C%7C%7Cdsfs%3D%3E335%7C%7C%7Cnps%3D%3E2; s_rfd=cdh%3D%3E27a30245%7C%7C%7Ctrd%3D%3Emax.book118.com%7C%7C%7Cftrd%3D%3Ebook118.com; s_s=cdh%3D%3E27a30245%7C%7C%7Clast_req%3D%3E1644844178%7C%7C%7Csid%3D%3E1644844178349860555%7C%7C%7Cdsps%3D%3E335",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"
}

headers_with_renrendoc = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    # ":authority:": "file1.renrendoc.com",
    "Cookie": "__yjs_duid=1_ff7344ac7a27f87e1156c4d085de6b4c1644844097298; Hm_lvt_ee26af2a7035c74326f5ac6c33ab7542=1644844099; Hm_lpvt_ee26af2a7035c74326f5ac6c33ab7542=1644844099",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"
}

def file_download(file_name, target_dirc, headers):
    with open(f"./util/{file_name}.txt", mode="r", encoding="utf8") as f:
        lines = f.readlines()
        index = 0
        for line in lines:
            index = index + 1
            print(f"line is {line}")
            result = requests.get(url=line.strip(), headers=headers, verify=False)
            print(result.status_code)
            result.raise_for_status()
            with open(f"./util/{target_dirc}/{str(index)}.png", mode="wb") as new:
                new.write(result.content)

def convert_base64_to_png():
    with open("./util/imgbase64.txt", mode="r", encoding="utf8") as f:
        lines = f.readlines()
        index = 0
        for line in lines:
            index = index + 1
            final = line[len("data:image/png;base64,"):].strip()
            image_data = base64.b64decode(final)
            with open(f"./util/关于安置房回迁工作实施方案-2464485741.html/{index}.png", mode="wb") as new:
                new.write(image_data)

if __name__ == "__main__":
    # png download and save
    # file_download(file_name = "links-png", target_dirc = "回迁安置方案-70084874.shtm", headers = headers_with_book118)

    # base64 to png
    # convert_base64_to_png()

    # renrendoc
    file_download(file_name = "links-gif", target_dirc = "关于安置房回迁工作实施方案-97554838.html", headers = headers_with_renrendoc)
