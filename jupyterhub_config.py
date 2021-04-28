# Example configuration file for jupyterhub.

## Set logging to debug for testing
c.Application.log_level = 'DEBUG'

## Custom logo file
c.JupyterHub.logo_file = '/home/ubuntu/jhubui/extra-assets/images/illumidesk.png'

## Custom template paths
c.JupyterHub.template_paths = ['/home/ubuntu/jhubui/templates', '/usr/local/share/jupyter/hub/custom_templates']

## Create a list of services to display service menu
c.JupyterHub.services = [
    {
        'name': 'my-service1',
        'url': 'http://host:8888',
        'admin': True,
        'api_token': 'super-secret',
    },
    {
        'name': 'my-service2',
        'url': 'http://host:8889',
        'admin': True,
        'api_token': 'super-secret',
    },
    {
        'name': 'my-service3',
        'url': 'http://host:8810',
        'admin': True,
        'api_token': 'super-secret',
    },
]

## Authenticator class
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'

## Spawner class used for testing
c.JupyterHub.spawner_class = 'jupyterhub.spawner.SimpleLocalProcessSpawner'
