# build stage
FROM node:16.3.0-alpine as build-stage
WORKDIR /app
COPY . /app
RUN npm install
CMD ["npm", "run", "build"]