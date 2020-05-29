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
                    ), label="População por Ano e Estado")
            ])
        ], style={'height' : '100vh', 'padding': '0px'})

altair = html.Div([
            html.Iframe(
                id='plot-altair',
                sandbox='allow-scripts',

                srcDoc=altair_visualization,

                style={'borderWidth': '0px', 'width' : '100%', 'height' : '100vh', 'padding': '0px'}
            )     
        ], style={'height' : '100vh', 'padding': '0px'})

pages = {'altair' : altair,
         'tableau' : tableau,
         'power_bi' : power_bi}