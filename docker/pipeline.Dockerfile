ARG GCP_REGISTRY_PROJECT
ARG BASE_FE_IMAGE_VERSION

# Compiles pipeline code
FROM slam_base_fe:$BASE_FE_IMAGE_VERSION as pipeline
WORKDIR /dep/pipeline/
COPY ui/pipeline /dep/pipeline
RUN ng build --prod --deployUrl=ui-assets/ --sourceMap=false --buildOptimizer=true
