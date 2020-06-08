import dash_core_components as dcc
import dash_html_components as html

tableau = html.Div([
            dcc.Tabs([
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts',
                        
                        src="https://public.tableau.com/views/CensusBrazil2010/Painel1?:display_count=y&publish=yes&:origin=viz_share_link:showVizHome=no&:embed=true",
            
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    )
                , label="População por Ano e Estado"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts',

                        src="https://public.tableau.com/shared/CQ3TSX555?:display_count=y&:origin=viz_share_link:showVizHome=no&:embed=true",
            
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    )
                , label="Mapa População"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts',

                        src="https://public.tableau.com/views/CensusBrazil2010-BarsPopulation/Painel3?:display_count=y&publish=yes&:origin=viz_share_link:showVizHome=no&:embed=true",
            
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    )
                , label="Barras População"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts',

                        src="https://public.tableau.com/views/CensusBrazil2010-StackedAgePopulation/Painel2?:display_count=y&:origin=viz_share_link:showVizHome=no&:embed=true",
            
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    )
                , label="População por Idade", id="black-border"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts',

                        src="https://public.tableau.com/views/CensusBrazil2010-MapsResidences/Painel6?:display_count=y&publish=yes&:origin=viz_share_link:showVizHome=no&:embed=true",
            
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    ), label="Mapa Domicílios"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts allow-popups',

                        src="https://public.tableau.com/views/CensusBrazil2010-CirclesResidences/Painel4?:display_count=y&publish=yes&:origin=viz_share_link:showVizHome=no&:embed=true",
            
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                    )
                , label="Domicílios por Estado e Categoria"),
                
                
            ])
        ], style={'height' : '100vh', 'padding': '0px'})

power_bi = html.Div([
            dcc.Tabs([
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-popups allow-forms allow-downloads',

                        src="https://app.powerbi.com/reportEmbed?reportId=176dce97-cbdb-42a9-8e9c-58acd4f8beb0&autoAuth=true&ctid=8e9749c8-eb2c-4a24-bdf5-d4f3510f7622&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1iLXByaW1hcnktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '80vh', 'padding': '0px'}
                    ), label="População por Ano e Estado"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts allow-popups allow-forms allow-cross-origin',

                        src="https://app.powerbi.com/reportEmbed?reportId=604baa68-bb74-419b-a37a-017b70d8191e&autoAuth=true&ctid=8e9749c8-eb2c-4a24-bdf5-d4f3510f7622&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1iLXByaW1hcnktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '80vh', 'padding': '0px'}
                    ), label="Mapa População"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts allow-popups allow-forms allow-cross-origin',

                        src="https://app.powerbi.com/reportEmbed?reportId=a42bc770-2706-47db-9261-4a432dd56b50&autoAuth=true&ctid=8e9749c8-eb2c-4a24-bdf5-d4f3510f7622&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1iLXByaW1hcnktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '80vh', 'padding': '0px'}
                    ), label="Barras População"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts allow-popups allow-forms allow-cross-origin',

                        src="https://app.powerbi.com/reportEmbed?reportId=153de6be-a79f-42b6-8b3a-ce2ea150f5f8&autoAuth=true&ctid=8e9749c8-eb2c-4a24-bdf5-d4f3510f7622&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1iLXByaW1hcnktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '80vh', 'padding': '0px'}
                    ), label="População por Idade"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts allow-popups allow-forms allow-cross-origin',

                        src="https://app.powerbi.com/reportEmbed?reportId=bd841c94-5167-44fb-8061-4dfee4260daa&autoAuth=true&ctid=8e9749c8-eb2c-4a24-bdf5-d4f3510f7622&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1iLXByaW1hcnktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '80vh', 'padding': '0px'}
                    ), label="Mapa Domicílios"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        sandbox='allow-same-origin allow-scripts allow-popups allow-forms allow-cross-origin',

                        src="https://app.powerbi.com/reportEmbed?reportId=4551a5b3-706b-4345-bf5a-71c2b6987d51&autoAuth=true&ctid=8e9749c8-eb2c-4a24-bdf5-d4f3510f7622&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWJyYXppbC1zb3V0aC1iLXByaW1hcnktcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '80vh', 'padding': '0px'}
                    ), label="Domicílios por Estado e Categoria"),           
            ])
        ], style={'height' : '100vh', 'padding': '0px'})
        
zoho = html.Div([
            dcc.Tabs([
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        #sandbox='allow-same-origin allow-scripts allow-popups allow-forms',

                        src="https://analytics.zoho.com/open-view/2255331000000003112",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                ), label="População por Ano e Estado"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        #sandbox='allow-same-origin allow-scripts allow-popups allow-forms',

                        src="https://analytics.zoho.com/open-view/2251342000000003775",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                ), label="Mapa População"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        #sandbox='allow-same-origin allow-scripts allow-popups allow-forms',

                        src="https://analytics.zoho.com/open-view/2251342000000003297",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                ), label="Barras População"),
                dcc.Tab(
                    html.Iframe(
                        id='plot',
                        #sandbox='allow-same-origin allow-scripts allow-popups allow-forms',

                        src="https://analytics.zoho.com/open-view/2252342000000003772",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                ), label="População por Idade"),
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

                        src="https://analytics.zoho.com/open-view/2240641000000003762",
                    
                        style={'borderWidth': '0px', 'width' : '100%', 'height' : '85vh', 'padding': '0px'}
                ), label="Domicílios por Estado e Categoria"),
            ])
        ], style={'height' : '100vh', 'padding': '0px'})

pages = {'zoho' : zoho,
         'tableau' : tableau,
         'power_bi' : power_bi}