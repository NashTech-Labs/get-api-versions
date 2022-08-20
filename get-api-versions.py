from kubernetes import client, utils 
import kubernetes.client
from kubernetes.client import ApiClient

from kubernetes.client.rest import ApiException
from kubernetes import client, config

def __get_kubernetes_client(bearer_token,api_server_endpoint):
    try:
        configuration = kubernetes.client.Configuration()
        configuration.host = api_server_endpoint
        configuration.verify_ssl = False
        configuration.api_key = {"authorization": "Bearer " + bearer_token}
        client.Configuration.set_default(configuration)
        with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
            api_instance1 = kubernetes.client.ApisApi(api_client)
        return api_instance1

    except ApiException as e:
        print("Error getting kubernetes client:\n{}".format(e.body))
        print("TYPE :{}".format(type(e)))
        return None


def get_api_versions(cluster_details):
        client_api= __get_kubernetes_client(
            bearer_token=cluster_details["bearer_token"],
            api_server_endpoint=cluster_details["api_server_endpoint"],
        )
      
        api_version =client_api.get_api_versions()
        print("get the list of all api versions: {}".format(api_version))
       
if __name__ == '__main__':
    cluster_details={
        "bearer_token":"Cluster-Bearer-Token",
        "api_server_endpoint":"Ip-k8s-control-plane"
    }
    get_api_versions(cluster_details)




