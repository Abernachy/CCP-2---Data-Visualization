import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,  LightenStyle as LS

# Make an api call and store the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:", r.status_code)

# store the api response in a variable
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    # get the project description if one is available
    description = repo_dict['description']
    if not description:
        description = "No description provided"
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'], 
        }
    plot_dicts.append(plot_dict)
    
# Make the visualization
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config,  style=my_style)
chart.title = 'Most Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_reposvisual.svg')
    # This piece of shit does not want to seem to work.  Not sure why it keeps giving errors, code matches instructor file
    # Nvm, I'm just a dumb fuck, forgot to change 'description' from it's old label