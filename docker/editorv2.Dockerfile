ARG GCP_REGISTRY_PROJECT
ARG BASE_FE_IMAGE_VERSION

# Compiles Editor V2 code
FROM slam_base_fe:$BASE_FE_IMAGE_VERSION as editorV2
WORKDIR /dep/react-planner
COPY /docker/.env /dep/react-planner/.env
COPY /docker/.env.local /dep/react-planner/.env.local
COPY /ui/react-planner /dep/react-planner
ENV NODE_OPTIONS=--max-old-space-size=6144
RUN npm run build