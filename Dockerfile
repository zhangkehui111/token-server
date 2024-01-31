# 基础镜像基础
FROM python:3.8.5
#指定环境变量
ENV PYTHONUNBUFFERED 1
#新建app文件夹
RUN mkdir /app
#指定工作目录
WORKDIR /app

#拷贝当前所有文件到工作目录
COPY . /app

#执行命令, 安装必要的包
RUN pip install --upgrade pip
#RUN pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn -r requirements.txt

#设置需要暴露的端口
EXPOSE 6666

CMD uvicorn main:app --host="0.0.0.0" --port=6666
