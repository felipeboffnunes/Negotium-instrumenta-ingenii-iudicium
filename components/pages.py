import dash_core_components as dcc
import dash_html_components as html

from components.altair.altair_visualization import altair_visualization

tableau = html.Div([
            dcc.Tabs([
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts',
                        
                        src="https://public.tableau.com/views/CensusBrazil2010/Painel1?:display_count=y&publish=yes&:origin=viz_share_link:showVizHome=no&:embed=true",
            
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    )
                , label="Timeseries Population"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts',

                        src="https://public.tableau.com/views/CensusBrazil2010-StackedAgePopulation/Painel2?:display_count=y&:origin=viz_share_link:showVizHome=no&:embed=true",
            
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    )
                , label="Stacked Age Population", id="black-border"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts',

                        src="https://public.tableau.com/views/CensusBrazil2010-BarsPopulation/Painel3?:display_count=y&publish=yes&:origin=viz_share_link:showVizHome=no&:embed=true",
            
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    )
                , label="Bars Population"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts',

                        src="https://public.tableau.com/views/CensusBrazil2010-CirclesResidences/Painel4?:display_count=y&publish=yes&:origin=viz_share_link:showVizHome=no&:embed=true",
            
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    )
                , label="Circles Residences"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts',

                        src="https://public.tableau.com/shared/CQ3TSX555?:display_count=y&:origin=viz_share_link:showVizHome=no&:embed=true",
            
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    )
                , label="Maps Population"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts',

                        src="https://public.tableau.com/views/CensusBrazil2010-MapsResidences/Painel6?:display_count=y&publish=yes&:origin=viz_share_link:showVizHome=no&:embed=true",
            
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    ), label="Maps Residences"),
            ])
        ], style={'height' : '100vh', 'padding': '0px'})

power_bi = html.Div([
            dcc.Tabs([
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts allow-popups allow-forms allow-cross-origin',

                        src="https://app.powerbi.com/reportEmbed?reportId=1bc58b44-49a5-4986-902b-45de42f4d5bb&autoAuth=true&ctid=51ebcf31-5839-412e-83bb-801a2ba78627&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldC8ifQ%3D%3D",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    ), label="População por Ano e Estado"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts allow-popups allow-forms allow-cross-origin',

                        src="https://app.powerbi.com/reportEmbed?reportId=350246cf-b777-4a83-9b67-6b2503a8424c&autoAuth=true&ctid=51ebcf31-5839-412e-83bb-801a2ba78627&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldC8ifQ%3D%3D",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    ), label="Domicílios por Estado e Categoria"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts allow-popups allow-forms allow-cross-origin',

                        src="https://app.powerbi.com/reportEmbed?reportId=425b03a7-7b37-43d2-ac73-33a34a8e9e46&autoAuth=true&ctid=51ebcf31-5839-412e-83bb-801a2ba78627&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldC8ifQ%3D%3D",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    ), label="Barras População"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts allow-popups allow-forms allow-cross-origin',

                        src="https://app.powerbi.com/reportEmbed?reportId=83003062-249b-48bf-94b8-e583212296f9&autoAuth=true&ctid=51ebcf31-5839-412e-83bb-801a2ba78627&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldC8ifQ%3D%3D",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    ), label="Mapa População"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts allow-popups allow-forms allow-cross-origin',

                        src="https://app.powerbi.com/reportEmbed?reportId=3ed8ce18-db14-429f-b898-27df3665b06d&autoAuth=true&ctid=51ebcf31-5839-412e-83bb-801a2ba78627&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldC8ifQ%3D%3D",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    ), label="Mapa Domicílios"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts allow-popups allow-forms allow-cross-origin',

                        src="https://app.powerbi.com/reportEmbed?reportId=c4278dba-e164-4763-8854-a8f14402fe4e&autoAuth=true&ctid=51ebcf31-5839-412e-83bb-801a2ba78627&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldC8ifQ%3D%3D",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    ), label="População por Idade")
            ])
        ], style={'height' : '100vh', 'padding': '0px'})
        
zoho = html.Div([
            dcc.Tabs([
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        #sandbox='allow-same-origin allow-scripts allow-popups allow-forms',

                        src="https://analytics.zoho.com/open-view/2237381000000004442",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    ), label="População por Idade e Região"),
                    dcc.Tab(
                    html.Iframe(
                        id='plot',
                        #sandbox='allow-same-origin allow-scripts allow-popups allow-forms',

                        src="https://analytics.zoho.com/open-view/2237381000000004952/a8ea56c880aed24e60b48af7315e445f",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    ), label="Mapa Domicílios"),
                    dcc.Tab(
                    html.Iframe(
                        id='plot',
                        #sandbox='allow-same-origin allow-scripts allow-popups allow-forms',

                        src="https://analytics.zoho.com/open-view/2237381000000007048",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    ), label="Mapa População"),
                    dcc.Tab(
                    html.Iframe(
                        id='plot',
                        #sandbox='allow-same-origin allow-scripts allow-popups allow-forms',

                        src="https://analytics.zoho.com/open-view/2240641000000003762",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    ), label="Barra Domicílios"),
            ])
        ], style={'height' : '100vh', 'padding': '0px'})

pages = {'zoho' : zoho,
         'tableau' : tableau,
         'power_bi' : power_bi}