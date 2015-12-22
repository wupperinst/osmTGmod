###################################################################################
#                                                                                 #
#   Copyright "2015" "Wuppertal Institut"                                         #
#                                                                                 #
#   Licensed under the Apache License, Version 2.0 (the "License");               #
#   you may not use this file except in compliance with the License.              #
#   You may obtain a copy of the License at                                       #
#                                                                                 #
#       http://www.apache.org/licenses/LICENSE-2.0                                #
#                                                                                 #
#   Unless required by applicable law or agreed to in writing, software           #
#   distributed under the License is distributed on an "AS IS" BASIS,             #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.      #
#   See the License for the specific language governing permissions and           #
#   limitations under the License.                                                #
#                                                                                 #
###################################################################################
import os


def write_projects(database,
                    password,
                    host,
                    port,
                    user):

    qgis_proj_dir = os.path.dirname(os.getcwd()) + "/qgis_projects"# gets one above current wd and then other folder


    result_project = """

    <!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
    <qgis projectname="" version="2.10.1-Pisa">
      <title></title>
      <layer-tree-group expanded="1" checked="Qt::PartiallyChecked" name="">
        <customproperties/>
        <layer-tree-layer expanded="1" checked="Qt::Checked" id="view_bus_data20151217121906009" name="view_bus_data">
          <customproperties/>
        </layer-tree-layer>
        <layer-tree-layer expanded="1" checked="Qt::Checked" id="view_branch_data20151217133637741" name="view_branch_data">
          <customproperties/>
        </layer-tree-layer>
        <layer-tree-layer expanded="1" checked="Qt::Checked" id="view_dcline_data20151217133332218" name="view_dcline_data">
          <customproperties/>
        </layer-tree-layer>
        <layer-tree-layer expanded="1" checked="Qt::Unchecked" id="view_problem_log20151217121906087" name="view_problem_log">
          <customproperties/>
        </layer-tree-layer>
        <layer-tree-layer expanded="1" checked="Qt::Checked" id="view_substations20151217121906140" name="view_substations">
          <customproperties/>
        </layer-tree-layer>
      </layer-tree-group>
      <relations/>
      <mapcanvas>
        <units>degrees</units>
        <extent>
          <xmin>5.67446690360767469</xmin>
          <ymin>47.15859863826560883</ymin>
          <xmax>15.04628747357738838</xmax>
          <ymax>55.14285135188627152</ymax>
        </extent>
        <rotation>0</rotation>
        <projections>0</projections>
        <destinationsrs>
          <spatialrefsys>
            <proj4>+proj=longlat +datum=WGS84 +no_defs</proj4>
            <srsid>3452</srsid>
            <srid>4326</srid>
            <authid>EPSG:4326</authid>
            <description>WGS 84</description>
            <projectionacronym>longlat</projectionacronym>
            <ellipsoidacronym>WGS84</ellipsoidacronym>
            <geographicflag>true</geographicflag>
          </spatialrefsys>
        </destinationsrs>
        <layer_coordinate_transform_info/>
      </mapcanvas>
      <visibility-presets/>
      <layer-tree-canvas>
        <custom-order enabled="0">
          <item>view_bus_data20151217121906009</item>
          <item>view_problem_log20151217121906087</item>
          <item>view_substations20151217121906140</item>
              <item>view_dcline_data20151217133332218</item>
          <item>view_branch_data20151217133637741</item>
        </custom-order>
      </layer-tree-canvas>
      <legend updateDrawingOrder="true">
        <legendlayer drawingOrder="-1" open="true" checked="Qt::Checked" name="view_bus_data" showFeatureCount="0">
          <filegroup open="true" hidden="false">
            <legendlayerfile isInOverview="0" layerid="view_bus_data20151217121906009" visible="1"/>
          </filegroup>
        </legendlayer>
        <legendlayer drawingOrder="-1" open="true" checked="Qt::Checked" name="view_branch_data" showFeatureCount="0">
          <filegroup open="true" hidden="false">
            <legendlayerfile isInOverview="0" layerid="view_branch_data20151217133637741" visible="1"/>
          </filegroup>
        </legendlayer>
        <legendlayer drawingOrder="-1" open="true" checked="Qt::Checked" name="view_dcline_data" showFeatureCount="0">
          <filegroup open="true" hidden="false">
            <legendlayerfile isInOverview="0" layerid="view_dcline_data20151217133332218" visible="1"/>
          </filegroup>
        </legendlayer>
        <legendlayer drawingOrder="-1" open="true" checked="Qt::Unchecked" name="view_problem_log" showFeatureCount="0">
          <filegroup open="true" hidden="false">
            <legendlayerfile isInOverview="0" layerid="view_problem_log20151217121906087" visible="0"/>
          </filegroup>
        </legendlayer>
        <legendlayer drawingOrder="-1" open="true" checked="Qt::Checked" name="view_substations" showFeatureCount="0">
          <filegroup open="true" hidden="false">
            <legendlayerfile isInOverview="0" layerid="view_substations20151217121906140" visible="1"/>
          </filegroup>
        </legendlayer>
      </legend>
      <projectlayers layercount="5">
        <maplayer minimumScale="-4.65661e-10" maximumScale="1e+08" simplifyDrawingHints="1" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" geometry="Line" simplifyMaxScale="1" type="vector" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
          <id>view_branch_data20151217133637741</id>
          <datasource>dbname='"""+database+"""' host="""+host+""" port="""+port+""" user='"""+user+"""' password='"""+password+"""' sslmode=disable key='view_id' srid=4326 type=MultiLineString table="results"."view_branch_data" (geom) sql=</datasource>
          <title></title>
          <abstract></abstract>
          <keywordList>
            <value></value>
          </keywordList>
          <layername>view_branch_data</layername>
          <srs>
            <spatialrefsys>
              <proj4>+proj=longlat +datum=WGS84 +no_defs</proj4>
              <srsid>3452</srsid>
              <srid>4326</srid>
              <authid>EPSG:4326</authid>
              <description>WGS 84</description>
              <projectionacronym>longlat</projectionacronym>
              <ellipsoidacronym>WGS84</ellipsoidacronym>
              <geographicflag>true</geographicflag>
            </spatialrefsys>
          </srs>
          <provider encoding="UTF-8">postgres</provider>
          <previewExpression>COALESCE("relation_ids", '&lt;NULL>')</previewExpression>
          <vectorjoins/>
          <expressionfields/>
          <map-layer-style-manager current="">
            <map-layer-style name=""/>
          </map-layer-style-manager>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="result_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="view_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="f_bus">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="t_bus">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="br_r">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="br_x">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="br_b">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="rate_a">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="rate_b">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="rate_c">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="tap">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="shift">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="br_status">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="link_type">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="branch_voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
          <renderer-v2 symbollevels="0" type="RuleRenderer">
            <rules key="{18fa568f-4887-48df-832e-32e09f18cf55}">
              <rule filter=" &quot;branch_voltage&quot; >= 380000 AND link_type = 'line'" key="{fb6cf3fa-a11d-4246-915a-57f1abc40a4a}" symbol="0" label=">= 380"/>
              <rule filter=" &quot;branch_voltage&quot; = 220000 AND link_type= 'line'" key="{d84c0c58-913e-4424-9343-8eb90ab7465e}" symbol="1" label="220 kV"/>
              <rule filter="link_type= 'cable'" key="{db5cbfb8-beb8-4d3c-8349-559cb35844a1}" symbol="2" label="Erdkabel"/>
              <rule filter=" link_type  =  'transformer' " key="{3d4ecf28-828a-4557-97be-f6433c5d5837}" symbol="3" label="Transformator"/>
            </rules>
            <symbols>
              <symbol alpha="1" clip_to_extent="1" type="line" name="0">
                <layer pass="2" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="255,127,0,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="0.4"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="1">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="51,160,44,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="0.4"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="2">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="0,0,0,255"/>
                  <prop k="line_style" v="dot"/>
                  <prop k="line_width" v="0.4"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="3">
                <layer pass="1" class="MarkerLine" locked="0">
                  <prop k="interval" v="3"/>
                  <prop k="interval_map_unit_scale" v="0,0"/>
                  <prop k="interval_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_along_line" v="0"/>
                  <prop k="offset_along_line_map_unit_scale" v="0,0"/>
                  <prop k="offset_along_line_unit" v="MM"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="placement" v="vertex"/>
                  <prop k="rotate" v="1"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                  <symbol alpha="1" clip_to_extent="1" type="marker" name="@3@0">
                    <layer pass="0" class="SimpleMarker" locked="0">
                      <prop k="angle" v="0"/>
                      <prop k="color" v="187,51,53,255"/>
                      <prop k="horizontal_anchor_point" v="1"/>
                      <prop k="name" v="circle"/>
                      <prop k="offset" v="0,0"/>
                      <prop k="offset_map_unit_scale" v="0,0"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="outline_color" v="0,0,0,0"/>
                      <prop k="outline_style" v="solid"/>
                      <prop k="outline_width" v="0"/>
                      <prop k="outline_width_map_unit_scale" v="0,0"/>
                      <prop k="outline_width_unit" v="MM"/>
                      <prop k="scale_method" v="area"/>
                      <prop k="size" v="2.4"/>
                      <prop k="size_map_unit_scale" v="0,0"/>
                      <prop k="size_unit" v="MM"/>
                      <prop k="vertical_anchor_point" v="1"/>
                      <effect enabled="0" type="effectStack">
                        <effect type="dropShadow">
                          <prop k="blend_mode" v="13"/>
                          <prop k="blur_level" v="10"/>
                          <prop k="color" v="0,0,0,255"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="offset_angle" v="135"/>
                          <prop k="offset_distance" v="2"/>
                          <prop k="offset_unit" v="MM"/>
                          <prop k="offset_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0"/>
                        </effect>
                        <effect type="outerGlow">
                          <prop k="blend_mode" v="0"/>
                          <prop k="blur_level" v="3"/>
                          <prop k="color1" v="0,0,255,255"/>
                          <prop k="color2" v="0,255,0,255"/>
                          <prop k="color_type" v="0"/>
                          <prop k="discrete" v="0"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="single_color" v="255,255,255,255"/>
                          <prop k="spread" v="2"/>
                          <prop k="spread_unit" v="MM"/>
                          <prop k="spread_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0.5"/>
                        </effect>
                        <effect type="drawSource">
                          <prop k="blend_mode" v="0"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="1"/>
                          <prop k="transparency" v="0"/>
                        </effect>
                        <effect type="innerShadow">
                          <prop k="blend_mode" v="13"/>
                          <prop k="blur_level" v="10"/>
                          <prop k="color" v="0,0,0,255"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="offset_angle" v="135"/>
                          <prop k="offset_distance" v="2"/>
                          <prop k="offset_unit" v="MM"/>
                          <prop k="offset_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0"/>
                        </effect>
                        <effect type="innerGlow">
                          <prop k="blend_mode" v="0"/>
                          <prop k="blur_level" v="3"/>
                          <prop k="color1" v="0,0,255,255"/>
                          <prop k="color2" v="0,255,0,255"/>
                          <prop k="color_type" v="0"/>
                          <prop k="discrete" v="0"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="single_color" v="255,255,255,255"/>
                          <prop k="spread" v="2"/>
                          <prop k="spread_unit" v="MM"/>
                          <prop k="spread_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0.5"/>
                        </effect>
                      </effect>
                    </layer>
                  </symbol>
                </layer>
              </symbol>
            </symbols>
            <effect enabled="0" type="effectStack">
              <effect type="dropShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="outerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
              <effect type="drawSource">
                <prop k="blend_mode" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="1"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
            </effect>
          </renderer-v2>
          <customproperties>
            <property key="labeling" value="pal"/>
            <property key="labeling/addDirectionSymbol" value="false"/>
            <property key="labeling/angleOffset" value="0"/>
            <property key="labeling/blendMode" value="0"/>
            <property key="labeling/bufferBlendMode" value="0"/>
            <property key="labeling/bufferColorA" value="255"/>
            <property key="labeling/bufferColorB" value="255"/>
            <property key="labeling/bufferColorG" value="255"/>
            <property key="labeling/bufferColorR" value="255"/>
            <property key="labeling/bufferDraw" value="false"/>
            <property key="labeling/bufferJoinStyle" value="64"/>
            <property key="labeling/bufferNoFill" value="false"/>
            <property key="labeling/bufferSize" value="1"/>
            <property key="labeling/bufferSizeInMapUnits" value="false"/>
            <property key="labeling/bufferSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/bufferSizeMapUnitMinScale" value="0"/>
            <property key="labeling/bufferTransp" value="0"/>
            <property key="labeling/centroidInside" value="false"/>
            <property key="labeling/centroidWhole" value="false"/>
            <property key="labeling/decimals" value="3"/>
            <property key="labeling/displayAll" value="false"/>
            <property key="labeling/dist" value="0"/>
            <property key="labeling/distInMapUnits" value="false"/>
            <property key="labeling/distMapUnitMaxScale" value="0"/>
            <property key="labeling/distMapUnitMinScale" value="0"/>
            <property key="labeling/enabled" value="false"/>
            <property key="labeling/fieldName" value=""/>
            <property key="labeling/fontBold" value="false"/>
            <property key="labeling/fontCapitals" value="0"/>
            <property key="labeling/fontFamily" value="Lucida Grande"/>
            <property key="labeling/fontItalic" value="false"/>
            <property key="labeling/fontLetterSpacing" value="0"/>
            <property key="labeling/fontLimitPixelSize" value="false"/>
            <property key="labeling/fontMaxPixelSize" value="10000"/>
            <property key="labeling/fontMinPixelSize" value="3"/>
            <property key="labeling/fontSize" value="8.25"/>
            <property key="labeling/fontSizeInMapUnits" value="false"/>
            <property key="labeling/fontSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/fontSizeMapUnitMinScale" value="0"/>
            <property key="labeling/fontStrikeout" value="false"/>
            <property key="labeling/fontUnderline" value="false"/>
            <property key="labeling/fontWeight" value="50"/>
            <property key="labeling/fontWordSpacing" value="0"/>
            <property key="labeling/formatNumbers" value="false"/>
            <property key="labeling/isExpression" value="true"/>
            <property key="labeling/labelOffsetInMapUnits" value="true"/>
            <property key="labeling/labelOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/labelOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/labelPerPart" value="false"/>
            <property key="labeling/leftDirectionSymbol" value="&lt;"/>
            <property key="labeling/limitNumLabels" value="false"/>
            <property key="labeling/maxCurvedCharAngleIn" value="20"/>
            <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
            <property key="labeling/maxNumLabels" value="2000"/>
            <property key="labeling/mergeLines" value="false"/>
            <property key="labeling/minFeatureSize" value="0"/>
            <property key="labeling/multilineAlign" value="0"/>
            <property key="labeling/multilineHeight" value="1"/>
            <property key="labeling/namedStyle" value="Normal"/>
            <property key="labeling/obstacle" value="true"/>
            <property key="labeling/placeDirectionSymbol" value="0"/>
            <property key="labeling/placement" value="2"/>
            <property key="labeling/placementFlags" value="10"/>
            <property key="labeling/plussign" value="false"/>
            <property key="labeling/preserveRotation" value="true"/>
            <property key="labeling/previewBkgrdColor" value="#ffffff"/>
            <property key="labeling/priority" value="5"/>
            <property key="labeling/quadOffset" value="4"/>
            <property key="labeling/repeatDistance" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMaxScale" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMinScale" value="0"/>
            <property key="labeling/repeatDistanceUnit" value="1"/>
            <property key="labeling/reverseDirectionSymbol" value="false"/>
            <property key="labeling/rightDirectionSymbol" value=">"/>
            <property key="labeling/scaleMax" value="10000000"/>
            <property key="labeling/scaleMin" value="1"/>
            <property key="labeling/scaleVisibility" value="false"/>
            <property key="labeling/shadowBlendMode" value="6"/>
            <property key="labeling/shadowColorB" value="0"/>
            <property key="labeling/shadowColorG" value="0"/>
            <property key="labeling/shadowColorR" value="0"/>
            <property key="labeling/shadowDraw" value="false"/>
            <property key="labeling/shadowOffsetAngle" value="135"/>
            <property key="labeling/shadowOffsetDist" value="1"/>
            <property key="labeling/shadowOffsetGlobal" value="true"/>
            <property key="labeling/shadowOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shadowOffsetUnits" value="1"/>
            <property key="labeling/shadowRadius" value="1.5"/>
            <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
            <property key="labeling/shadowRadiusMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowRadiusMapUnitMinScale" value="0"/>
            <property key="labeling/shadowRadiusUnits" value="1"/>
            <property key="labeling/shadowScale" value="100"/>
            <property key="labeling/shadowTransparency" value="30"/>
            <property key="labeling/shadowUnder" value="0"/>
            <property key="labeling/shapeBlendMode" value="0"/>
            <property key="labeling/shapeBorderColorA" value="255"/>
            <property key="labeling/shapeBorderColorB" value="128"/>
            <property key="labeling/shapeBorderColorG" value="128"/>
            <property key="labeling/shapeBorderColorR" value="128"/>
            <property key="labeling/shapeBorderWidth" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMinScale" value="0"/>
            <property key="labeling/shapeBorderWidthUnits" value="1"/>
            <property key="labeling/shapeDraw" value="false"/>
            <property key="labeling/shapeFillColorA" value="255"/>
            <property key="labeling/shapeFillColorB" value="255"/>
            <property key="labeling/shapeFillColorG" value="255"/>
            <property key="labeling/shapeFillColorR" value="255"/>
            <property key="labeling/shapeJoinStyle" value="64"/>
            <property key="labeling/shapeOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shapeOffsetUnits" value="1"/>
            <property key="labeling/shapeOffsetX" value="0"/>
            <property key="labeling/shapeOffsetY" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMinScale" value="0"/>
            <property key="labeling/shapeRadiiUnits" value="1"/>
            <property key="labeling/shapeRadiiX" value="0"/>
            <property key="labeling/shapeRadiiY" value="0"/>
            <property key="labeling/shapeRotation" value="0"/>
            <property key="labeling/shapeRotationType" value="0"/>
            <property key="labeling/shapeSVGFile" value=""/>
            <property key="labeling/shapeSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeSizeMapUnitMinScale" value="0"/>
            <property key="labeling/shapeSizeType" value="0"/>
            <property key="labeling/shapeSizeUnits" value="1"/>
            <property key="labeling/shapeSizeX" value="0"/>
            <property key="labeling/shapeSizeY" value="0"/>
            <property key="labeling/shapeTransparency" value="0"/>
            <property key="labeling/shapeType" value="0"/>
            <property key="labeling/textColorA" value="255"/>
            <property key="labeling/textColorB" value="0"/>
            <property key="labeling/textColorG" value="0"/>
            <property key="labeling/textColorR" value="0"/>
            <property key="labeling/textTransp" value="0"/>
            <property key="labeling/upsidedownLabels" value="0"/>
            <property key="labeling/wrapChar" value=""/>
            <property key="labeling/xOffset" value="0"/>
            <property key="labeling/yOffset" value="0"/>
          </customproperties>
          <blendMode>0</blendMode>
          <featureBlendMode>0</featureBlendMode>
          <layerTransparency>0</layerTransparency>
          <displayfield>relation_ids</displayfield>
          <label>0</label>
          <labelattributes>
            <label fieldname="" text="Beschriftung"/>
            <family fieldname="" name="MS Shell Dlg 2"/>
            <size fieldname="" units="pt" value="12"/>
            <bold fieldname="" on="0"/>
            <italic fieldname="" on="0"/>
            <underline fieldname="" on="0"/>
            <strikeout fieldname="" on="0"/>
            <color fieldname="" red="0" blue="0" green="0"/>
            <x fieldname=""/>
            <y fieldname=""/>
            <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
            <angle fieldname="" value="0" auto="0"/>
            <alignment fieldname="" value="center"/>
            <buffercolor fieldname="" red="255" blue="255" green="255"/>
            <buffersize fieldname="" units="pt" value="1"/>
            <bufferenabled fieldname="" on=""/>
            <multilineenabled fieldname="" on=""/>
            <selectedonly on=""/>
          </labelattributes>
          <SingleCategoryDiagramRenderer diagramType="Pie">
            <DiagramCategory penColor="#000000" labelPlacementMethod="XHeight" penWidth="0" diagramOrientation="Up" minimumSize="0" barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" backgroundColor="#ffffff" transparency="0" width="15" scaleDependency="Area" backgroundAlpha="255" angleOffset="1440" scaleBasedVisibility="0" enabled="0" height="15" sizeType="MM" minScaleDenominator="-4.65661e-10">
              <fontProperties description="Lucida Grande,13,-1,5,50,0,0,0,0,0" style=""/>
              <attribute field="" color="#000000" label=""/>
            </DiagramCategory>
          </SingleCategoryDiagramRenderer>
          <DiagramLayerSettings yPosColumn="-1" linePlacementFlags="10" placement="2" dist="0" xPosColumn="-1" priority="0" obstacle="0" showAll="1"/>
          <editform>../../../PROGRA~1/QGISWI~1/bin</editform>
          <editforminit/>
          <featformsuppress>0</featformsuppress>
          <annotationform>../../../PROGRA~1/QGISWI~1/bin</annotationform>
          <editorlayout>generatedlayout</editorlayout>
          <excludeAttributesWMS/>
          <excludeAttributesWFS/>
          <attributeactions/>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="result_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="view_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="f_bus">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="t_bus">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="br_r">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="br_x">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="br_b">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="rate_a">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="rate_b">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="rate_c">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="tap">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="shift">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="br_status">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="link_type">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="branch_voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
        </maplayer>
        <maplayer minimumScale="0" maximumScale="1e+08" simplifyDrawingHints="0" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" geometry="Point" simplifyMaxScale="1" type="vector" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
          <id>view_bus_data20151217121906009</id>
          <datasource>dbname='"""+database+"""' host="""+host+""" port="""+port+""" user='"""+user+"""' password='"""+password+"""' sslmode=disable key='view_id' srid=4326 type=Point table="results"."view_bus_data" (geom) sql=</datasource>
          <title></title>
          <abstract></abstract>
          <keywordList>
            <value></value>
          </keywordList>
          <layername>view_bus_data</layername>
          <srs>
            <spatialrefsys>
              <proj4>+proj=longlat +datum=WGS84 +no_defs</proj4>
              <srsid>3452</srsid>
              <srid>4326</srid>
              <authid>EPSG:4326</authid>
              <description>WGS 84</description>
              <projectionacronym>longlat</projectionacronym>
              <ellipsoidacronym>WGS84</ellipsoidacronym>
              <geographicflag>true</geographicflag>
            </spatialrefsys>
          </srs>
          <provider encoding="UTF-8">postgres</provider>
          <previewExpression></previewExpression>
          <vectorjoins/>
          <expressionfields/>
          <map-layer-style-manager current="">
            <map-layer-style name=""/>
          </map-layer-style-manager>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="result_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="view_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="bus_i">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="bus_type">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="pd">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qd">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="gs">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="bs">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="bus_area">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="vm">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="va">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="base_kv">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="zone">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="vmax">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="vmin">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="osm_substation_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="cntr_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="osm_name">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
          <renderer-v2 symbollevels="0" type="RuleRenderer">
            <rules key="{4a019d98-9843-463d-a59b-0514046fec8d}">
              <rule filter=" &quot;osm_substation_id&quot; IS NULL" key="{db87f334-0ae8-4ee2-bd21-9454c35f0567}" symbol="0" label="Einfacher Netzknoten"/>
              <rule filter="NOT  &quot;osm_substation_id&quot; IS NULL" key="{f847291a-f51b-4ae6-b45e-32b799fa6c0d}" symbol="1" label="Umspannwerk"/>
            </rules>
            <symbols>
              <symbol alpha="1" clip_to_extent="1" type="marker" name="0">
                <layer pass="0" class="SimpleMarker" locked="0">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="0,0,0,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="name" v="circle"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="0,0,0,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="0,0"/>
                  <prop k="outline_width_unit" v="MM"/>
                  <prop k="scale_method" v="area"/>
                  <prop k="size" v="0.8"/>
                  <prop k="size_map_unit_scale" v="0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="marker" name="1">
                <layer pass="0" class="SimpleMarker" locked="0">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="31,120,180,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="name" v="circle"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="0,0,0,0"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0.8"/>
                  <prop k="outline_width_map_unit_scale" v="0,0"/>
                  <prop k="outline_width_unit" v="MM"/>
                  <prop k="scale_method" v="area"/>
                  <prop k="size" v="2.3"/>
                  <prop k="size_map_unit_scale" v="0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
            </symbols>
            <effect enabled="0" type="effectStack">
              <effect type="dropShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="outerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
              <effect type="drawSource">
                <prop k="blend_mode" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="1"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
            </effect>
          </renderer-v2>
          <customproperties>
            <property key="labeling" value="pal"/>
            <property key="labeling/addDirectionSymbol" value="false"/>
            <property key="labeling/angleOffset" value="0"/>
            <property key="labeling/blendMode" value="0"/>
            <property key="labeling/bufferBlendMode" value="0"/>
            <property key="labeling/bufferColorA" value="255"/>
            <property key="labeling/bufferColorB" value="255"/>
            <property key="labeling/bufferColorG" value="255"/>
            <property key="labeling/bufferColorR" value="255"/>
            <property key="labeling/bufferDraw" value="false"/>
            <property key="labeling/bufferJoinStyle" value="64"/>
            <property key="labeling/bufferNoFill" value="false"/>
            <property key="labeling/bufferSize" value="1"/>
            <property key="labeling/bufferSizeInMapUnits" value="false"/>
            <property key="labeling/bufferSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/bufferSizeMapUnitMinScale" value="0"/>
            <property key="labeling/bufferTransp" value="0"/>
            <property key="labeling/centroidInside" value="false"/>
            <property key="labeling/centroidWhole" value="false"/>
            <property key="labeling/decimals" value="3"/>
            <property key="labeling/displayAll" value="false"/>
            <property key="labeling/dist" value="0"/>
            <property key="labeling/distInMapUnits" value="false"/>
            <property key="labeling/distMapUnitMaxScale" value="0"/>
            <property key="labeling/distMapUnitMinScale" value="0"/>
            <property key="labeling/enabled" value="false"/>
            <property key="labeling/fieldName" value=""/>
            <property key="labeling/fontBold" value="false"/>
            <property key="labeling/fontCapitals" value="0"/>
            <property key="labeling/fontFamily" value="Lucida Grande"/>
            <property key="labeling/fontItalic" value="false"/>
            <property key="labeling/fontLetterSpacing" value="0"/>
            <property key="labeling/fontLimitPixelSize" value="false"/>
            <property key="labeling/fontMaxPixelSize" value="10000"/>
            <property key="labeling/fontMinPixelSize" value="3"/>
            <property key="labeling/fontSize" value="8.25"/>
            <property key="labeling/fontSizeInMapUnits" value="false"/>
            <property key="labeling/fontSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/fontSizeMapUnitMinScale" value="0"/>
            <property key="labeling/fontStrikeout" value="false"/>
            <property key="labeling/fontUnderline" value="false"/>
            <property key="labeling/fontWeight" value="50"/>
            <property key="labeling/fontWordSpacing" value="0"/>
            <property key="labeling/formatNumbers" value="false"/>
            <property key="labeling/isExpression" value="true"/>
            <property key="labeling/labelOffsetInMapUnits" value="true"/>
            <property key="labeling/labelOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/labelOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/labelPerPart" value="false"/>
            <property key="labeling/leftDirectionSymbol" value="&lt;"/>
            <property key="labeling/limitNumLabels" value="false"/>
            <property key="labeling/maxCurvedCharAngleIn" value="20"/>
            <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
            <property key="labeling/maxNumLabels" value="2000"/>
            <property key="labeling/mergeLines" value="false"/>
            <property key="labeling/minFeatureSize" value="0"/>
            <property key="labeling/multilineAlign" value="0"/>
            <property key="labeling/multilineHeight" value="1"/>
            <property key="labeling/namedStyle" value="Normal"/>
            <property key="labeling/obstacle" value="true"/>
            <property key="labeling/placeDirectionSymbol" value="0"/>
            <property key="labeling/placement" value="0"/>
            <property key="labeling/placementFlags" value="0"/>
            <property key="labeling/plussign" value="false"/>
            <property key="labeling/preserveRotation" value="true"/>
            <property key="labeling/previewBkgrdColor" value="#ffffff"/>
            <property key="labeling/priority" value="5"/>
            <property key="labeling/quadOffset" value="4"/>
            <property key="labeling/repeatDistance" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMaxScale" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMinScale" value="0"/>
            <property key="labeling/repeatDistanceUnit" value="1"/>
            <property key="labeling/reverseDirectionSymbol" value="false"/>
            <property key="labeling/rightDirectionSymbol" value=">"/>
            <property key="labeling/scaleMax" value="10000000"/>
            <property key="labeling/scaleMin" value="1"/>
            <property key="labeling/scaleVisibility" value="false"/>
            <property key="labeling/shadowBlendMode" value="6"/>
            <property key="labeling/shadowColorB" value="0"/>
            <property key="labeling/shadowColorG" value="0"/>
            <property key="labeling/shadowColorR" value="0"/>
            <property key="labeling/shadowDraw" value="false"/>
            <property key="labeling/shadowOffsetAngle" value="135"/>
            <property key="labeling/shadowOffsetDist" value="1"/>
            <property key="labeling/shadowOffsetGlobal" value="true"/>
            <property key="labeling/shadowOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shadowOffsetUnits" value="1"/>
            <property key="labeling/shadowRadius" value="1.5"/>
            <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
            <property key="labeling/shadowRadiusMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowRadiusMapUnitMinScale" value="0"/>
            <property key="labeling/shadowRadiusUnits" value="1"/>
            <property key="labeling/shadowScale" value="100"/>
            <property key="labeling/shadowTransparency" value="30"/>
            <property key="labeling/shadowUnder" value="0"/>
            <property key="labeling/shapeBlendMode" value="0"/>
            <property key="labeling/shapeBorderColorA" value="255"/>
            <property key="labeling/shapeBorderColorB" value="128"/>
            <property key="labeling/shapeBorderColorG" value="128"/>
            <property key="labeling/shapeBorderColorR" value="128"/>
            <property key="labeling/shapeBorderWidth" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMinScale" value="0"/>
            <property key="labeling/shapeBorderWidthUnits" value="1"/>
            <property key="labeling/shapeDraw" value="false"/>
            <property key="labeling/shapeFillColorA" value="255"/>
            <property key="labeling/shapeFillColorB" value="255"/>
            <property key="labeling/shapeFillColorG" value="255"/>
            <property key="labeling/shapeFillColorR" value="255"/>
            <property key="labeling/shapeJoinStyle" value="64"/>
            <property key="labeling/shapeOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shapeOffsetUnits" value="1"/>
            <property key="labeling/shapeOffsetX" value="0"/>
            <property key="labeling/shapeOffsetY" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMinScale" value="0"/>
            <property key="labeling/shapeRadiiUnits" value="1"/>
            <property key="labeling/shapeRadiiX" value="0"/>
            <property key="labeling/shapeRadiiY" value="0"/>
            <property key="labeling/shapeRotation" value="0"/>
            <property key="labeling/shapeRotationType" value="0"/>
            <property key="labeling/shapeSVGFile" value=""/>
            <property key="labeling/shapeSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeSizeMapUnitMinScale" value="0"/>
            <property key="labeling/shapeSizeType" value="0"/>
            <property key="labeling/shapeSizeUnits" value="1"/>
            <property key="labeling/shapeSizeX" value="0"/>
            <property key="labeling/shapeSizeY" value="0"/>
            <property key="labeling/shapeTransparency" value="0"/>
            <property key="labeling/shapeType" value="0"/>
            <property key="labeling/textColorA" value="255"/>
            <property key="labeling/textColorB" value="0"/>
            <property key="labeling/textColorG" value="0"/>
            <property key="labeling/textColorR" value="0"/>
            <property key="labeling/textTransp" value="0"/>
            <property key="labeling/upsidedownLabels" value="0"/>
            <property key="labeling/wrapChar" value=""/>
            <property key="labeling/xOffset" value="0"/>
            <property key="labeling/yOffset" value="0"/>
          </customproperties>
          <blendMode>0</blendMode>
          <featureBlendMode>0</featureBlendMode>
          <layerTransparency>19</layerTransparency>
          <displayfield>id</displayfield>
          <label>0</label>
          <labelattributes>
            <label fieldname="" text="Beschriftung"/>
            <family fieldname="" name="MS Shell Dlg 2"/>
            <size fieldname="" units="pt" value="12"/>
            <bold fieldname="" on="0"/>
            <italic fieldname="" on="0"/>
            <underline fieldname="" on="0"/>
            <strikeout fieldname="" on="0"/>
            <color fieldname="" red="0" blue="0" green="0"/>
            <x fieldname=""/>
            <y fieldname=""/>
            <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
            <angle fieldname="" value="0" auto="0"/>
            <alignment fieldname="" value="center"/>
            <buffercolor fieldname="" red="255" blue="255" green="255"/>
            <buffersize fieldname="" units="pt" value="1"/>
            <bufferenabled fieldname="" on=""/>
            <multilineenabled fieldname="" on=""/>
            <selectedonly on=""/>
          </labelattributes>
          <SingleCategoryDiagramRenderer diagramType="Pie">
            <DiagramCategory penColor="#000000" labelPlacementMethod="XHeight" penWidth="0" diagramOrientation="Up" minimumSize="0" barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" backgroundColor="#ffffff" transparency="0" width="15" scaleDependency="Area" backgroundAlpha="255" angleOffset="1440" scaleBasedVisibility="0" enabled="0" height="15" sizeType="MM" minScaleDenominator="-4.65661e-10">
              <fontProperties description="Lucida Grande,13,-1,5,50,0,0,0,0,0" style=""/>
              <attribute field="" color="#000000" label=""/>
            </DiagramCategory>
          </SingleCategoryDiagramRenderer>
          <DiagramLayerSettings yPosColumn="-1" linePlacementFlags="10" placement="0" dist="0" xPosColumn="-1" priority="0" obstacle="0" showAll="1"/>
          <editform>../../../PROGRA~1/QGISWI~1/bin</editform>
          <editforminit/>
          <featformsuppress>0</featformsuppress>
          <annotationform>../../../PROGRA~1/QGISWI~1/bin</annotationform>
          <editorlayout>generatedlayout</editorlayout>
          <excludeAttributesWMS/>
          <excludeAttributesWFS/>
          <attributeactions/>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="result_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="view_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="bus_i">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="bus_type">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="pd">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qd">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="gs">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="bs">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="bus_area">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="vm">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="va">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="base_kv">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="zone">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="vmax">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="vmin">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="osm_substation_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="cntr_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="osm_name">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
        </maplayer>
        <maplayer minimumScale="0" maximumScale="1e+08" simplifyDrawingHints="1" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" geometry="Line" simplifyMaxScale="1" type="vector" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
          <id>view_dcline_data20151217133332218</id>
          <datasource>dbname='"""+database+"""' host="""+host+""" port="""+port+""" user='"""+user+"""' password='"""+password+"""' sslmode=disable key='view_id' srid=4326 type=MultiLineString table="results"."view_dcline_data" (geom) sql=</datasource>
          <title></title>
          <abstract></abstract>
          <keywordList>
            <value></value>
          </keywordList>
          <layername>view_dcline_data</layername>
          <srs>
            <spatialrefsys>
              <proj4>+proj=longlat +datum=WGS84 +no_defs</proj4>
              <srsid>3452</srsid>
              <srid>4326</srid>
              <authid>EPSG:4326</authid>
              <description>WGS 84</description>
              <projectionacronym>longlat</projectionacronym>
              <ellipsoidacronym>WGS84</ellipsoidacronym>
              <geographicflag>true</geographicflag>
            </spatialrefsys>
          </srs>
          <provider encoding="UTF-8">postgres</provider>
          <previewExpression></previewExpression>
          <vectorjoins/>
          <expressionfields/>
          <map-layer-style-manager current="">
            <map-layer-style name=""/>
          </map-layer-style-manager>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="result_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="view_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="f_bus">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="t_bus">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="br_status">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="pf">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="pt">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qf">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qt">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="vf">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="vt">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="pmin">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="pmax">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qminf">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qmaxf">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qmint">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qmaxt">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="loss0">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="loss1">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="link_type">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="branch_voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
          <renderer-v2 symbollevels="0" type="singleSymbol">
            <symbols>
              <symbol alpha="1" clip_to_extent="1" type="line" name="0">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="158,98,144,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="0.46"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
            </symbols>
            <rotation/>
            <sizescale scalemethod="diameter"/>
            <effect enabled="0" type="effectStack">
              <effect type="dropShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="outerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
              <effect type="drawSource">
                <prop k="blend_mode" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="1"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
            </effect>
          </renderer-v2>
          <customproperties>
            <property key="labeling" value="pal"/>
            <property key="labeling/addDirectionSymbol" value="false"/>
            <property key="labeling/angleOffset" value="0"/>
            <property key="labeling/blendMode" value="0"/>
            <property key="labeling/bufferBlendMode" value="0"/>
            <property key="labeling/bufferColorA" value="255"/>
            <property key="labeling/bufferColorB" value="255"/>
            <property key="labeling/bufferColorG" value="255"/>
            <property key="labeling/bufferColorR" value="255"/>
            <property key="labeling/bufferDraw" value="false"/>
            <property key="labeling/bufferJoinStyle" value="64"/>
            <property key="labeling/bufferNoFill" value="false"/>
            <property key="labeling/bufferSize" value="1"/>
            <property key="labeling/bufferSizeInMapUnits" value="false"/>
            <property key="labeling/bufferSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/bufferSizeMapUnitMinScale" value="0"/>
            <property key="labeling/bufferTransp" value="0"/>
            <property key="labeling/centroidInside" value="false"/>
            <property key="labeling/centroidWhole" value="false"/>
            <property key="labeling/decimals" value="3"/>
            <property key="labeling/displayAll" value="false"/>
            <property key="labeling/dist" value="0"/>
            <property key="labeling/distInMapUnits" value="false"/>
            <property key="labeling/distMapUnitMaxScale" value="0"/>
            <property key="labeling/distMapUnitMinScale" value="0"/>
            <property key="labeling/enabled" value="false"/>
            <property key="labeling/fieldName" value=""/>
            <property key="labeling/fontBold" value="false"/>
            <property key="labeling/fontCapitals" value="0"/>
            <property key="labeling/fontFamily" value="Lucida Grande"/>
            <property key="labeling/fontItalic" value="false"/>
            <property key="labeling/fontLetterSpacing" value="0"/>
            <property key="labeling/fontLimitPixelSize" value="false"/>
            <property key="labeling/fontMaxPixelSize" value="10000"/>
            <property key="labeling/fontMinPixelSize" value="3"/>
            <property key="labeling/fontSize" value="8.25"/>
            <property key="labeling/fontSizeInMapUnits" value="false"/>
            <property key="labeling/fontSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/fontSizeMapUnitMinScale" value="0"/>
            <property key="labeling/fontStrikeout" value="false"/>
            <property key="labeling/fontUnderline" value="false"/>
            <property key="labeling/fontWeight" value="50"/>
            <property key="labeling/fontWordSpacing" value="0"/>
            <property key="labeling/formatNumbers" value="false"/>
            <property key="labeling/isExpression" value="true"/>
            <property key="labeling/labelOffsetInMapUnits" value="true"/>
            <property key="labeling/labelOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/labelOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/labelPerPart" value="false"/>
            <property key="labeling/leftDirectionSymbol" value="&lt;"/>
            <property key="labeling/limitNumLabels" value="false"/>
            <property key="labeling/maxCurvedCharAngleIn" value="20"/>
            <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
            <property key="labeling/maxNumLabels" value="2000"/>
            <property key="labeling/mergeLines" value="false"/>
            <property key="labeling/minFeatureSize" value="0"/>
            <property key="labeling/multilineAlign" value="0"/>
            <property key="labeling/multilineHeight" value="1"/>
            <property key="labeling/namedStyle" value="Normal"/>
            <property key="labeling/obstacle" value="true"/>
            <property key="labeling/placeDirectionSymbol" value="0"/>
            <property key="labeling/placement" value="2"/>
            <property key="labeling/placementFlags" value="10"/>
            <property key="labeling/plussign" value="false"/>
            <property key="labeling/preserveRotation" value="true"/>
            <property key="labeling/previewBkgrdColor" value="#ffffff"/>
            <property key="labeling/priority" value="5"/>
            <property key="labeling/quadOffset" value="4"/>
            <property key="labeling/repeatDistance" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMaxScale" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMinScale" value="0"/>
            <property key="labeling/repeatDistanceUnit" value="1"/>
            <property key="labeling/reverseDirectionSymbol" value="false"/>
            <property key="labeling/rightDirectionSymbol" value=">"/>
            <property key="labeling/scaleMax" value="10000000"/>
            <property key="labeling/scaleMin" value="1"/>
            <property key="labeling/scaleVisibility" value="false"/>
            <property key="labeling/shadowBlendMode" value="6"/>
            <property key="labeling/shadowColorB" value="0"/>
            <property key="labeling/shadowColorG" value="0"/>
            <property key="labeling/shadowColorR" value="0"/>
            <property key="labeling/shadowDraw" value="false"/>
            <property key="labeling/shadowOffsetAngle" value="135"/>
            <property key="labeling/shadowOffsetDist" value="1"/>
            <property key="labeling/shadowOffsetGlobal" value="true"/>
            <property key="labeling/shadowOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shadowOffsetUnits" value="1"/>
            <property key="labeling/shadowRadius" value="1.5"/>
            <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
            <property key="labeling/shadowRadiusMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowRadiusMapUnitMinScale" value="0"/>
            <property key="labeling/shadowRadiusUnits" value="1"/>
            <property key="labeling/shadowScale" value="100"/>
            <property key="labeling/shadowTransparency" value="30"/>
            <property key="labeling/shadowUnder" value="0"/>
            <property key="labeling/shapeBlendMode" value="0"/>
            <property key="labeling/shapeBorderColorA" value="255"/>
            <property key="labeling/shapeBorderColorB" value="128"/>
            <property key="labeling/shapeBorderColorG" value="128"/>
            <property key="labeling/shapeBorderColorR" value="128"/>
            <property key="labeling/shapeBorderWidth" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMinScale" value="0"/>
            <property key="labeling/shapeBorderWidthUnits" value="1"/>
            <property key="labeling/shapeDraw" value="false"/>
            <property key="labeling/shapeFillColorA" value="255"/>
            <property key="labeling/shapeFillColorB" value="255"/>
            <property key="labeling/shapeFillColorG" value="255"/>
            <property key="labeling/shapeFillColorR" value="255"/>
            <property key="labeling/shapeJoinStyle" value="64"/>
            <property key="labeling/shapeOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shapeOffsetUnits" value="1"/>
            <property key="labeling/shapeOffsetX" value="0"/>
            <property key="labeling/shapeOffsetY" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMinScale" value="0"/>
            <property key="labeling/shapeRadiiUnits" value="1"/>
            <property key="labeling/shapeRadiiX" value="0"/>
            <property key="labeling/shapeRadiiY" value="0"/>
            <property key="labeling/shapeRotation" value="0"/>
            <property key="labeling/shapeRotationType" value="0"/>
            <property key="labeling/shapeSVGFile" value=""/>
            <property key="labeling/shapeSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeSizeMapUnitMinScale" value="0"/>
            <property key="labeling/shapeSizeType" value="0"/>
            <property key="labeling/shapeSizeUnits" value="1"/>
            <property key="labeling/shapeSizeX" value="0"/>
            <property key="labeling/shapeSizeY" value="0"/>
            <property key="labeling/shapeTransparency" value="0"/>
            <property key="labeling/shapeType" value="0"/>
            <property key="labeling/textColorA" value="255"/>
            <property key="labeling/textColorB" value="0"/>
            <property key="labeling/textColorG" value="0"/>
            <property key="labeling/textColorR" value="0"/>
            <property key="labeling/textTransp" value="0"/>
            <property key="labeling/upsidedownLabels" value="0"/>
            <property key="labeling/wrapChar" value=""/>
            <property key="labeling/xOffset" value="0"/>
            <property key="labeling/yOffset" value="0"/>
          </customproperties>
          <blendMode>0</blendMode>
          <featureBlendMode>0</featureBlendMode>
          <layerTransparency>0</layerTransparency>
          <displayfield>branch_id</displayfield>
          <label>0</label>
          <labelattributes>
            <label fieldname="" text="Label"/>
            <family fieldname="" name="MS Shell Dlg 2"/>
            <size fieldname="" units="pt" value="12"/>
            <bold fieldname="" on="0"/>
            <italic fieldname="" on="0"/>
            <underline fieldname="" on="0"/>
            <strikeout fieldname="" on="0"/>
            <color fieldname="" red="0" blue="0" green="0"/>
            <x fieldname=""/>
            <y fieldname=""/>
            <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
            <angle fieldname="" value="0" auto="0"/>
            <alignment fieldname="" value="center"/>
            <buffercolor fieldname="" red="255" blue="255" green="255"/>
            <buffersize fieldname="" units="pt" value="1"/>
            <bufferenabled fieldname="" on=""/>
            <multilineenabled fieldname="" on=""/>
            <selectedonly on=""/>
          </labelattributes>
          <SingleCategoryDiagramRenderer diagramType="Pie">
            <DiagramCategory penColor="#000000" labelPlacementMethod="XHeight" penWidth="0" diagramOrientation="Up" minimumSize="0" barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" backgroundColor="#ffffff" transparency="0" width="15" scaleDependency="Area" backgroundAlpha="255" angleOffset="1440" scaleBasedVisibility="0" enabled="0" height="15" sizeType="MM" minScaleDenominator="-4.65661e-10">
              <fontProperties description="Lucida Grande,13,-1,5,50,0,0,0,0,0" style=""/>
              <attribute field="" color="#000000" label=""/>
            </DiagramCategory>
          </SingleCategoryDiagramRenderer>
          <DiagramLayerSettings yPosColumn="-1" linePlacementFlags="10" placement="2" dist="0" xPosColumn="-1" priority="0" obstacle="0" showAll="1"/>
          <editform>.</editform>
          <editforminit/>
          <featformsuppress>0</featformsuppress>
          <annotationform>.</annotationform>
          <editorlayout>generatedlayout</editorlayout>
          <excludeAttributesWMS/>
          <excludeAttributesWFS/>
          <attributeactions/>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="result_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="view_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="f_bus">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="t_bus">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="br_status">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="pf">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="pt">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qf">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qt">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="vf">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="vt">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="pmin">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="pmax">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qminf">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qmaxf">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qmint">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="qmaxt">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="loss0">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="loss1">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="link_type">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="branch_voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
        </maplayer>
        <maplayer minimumScale="0" maximumScale="1e+08" simplifyDrawingHints="1" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" geometry="Line" simplifyMaxScale="1" type="vector" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
          <id>view_problem_log20151217121906087</id>
          <datasource>dbname='"""+database+"""' host="""+host+""" port="""+port+""" user='"""+user+"""' password='"""+password+"""' sslmode=disable key='view_id' srid=4326 type=MultiLineString table="results"."view_problem_log" (way) sql=</datasource>
          <title></title>
          <abstract></abstract>
          <keywordList>
            <value></value>
          </keywordList>
          <layername>view_problem_log</layername>
          <srs>
            <spatialrefsys>
              <proj4>+proj=longlat +datum=WGS84 +no_defs</proj4>
              <srsid>3452</srsid>
              <srid>4326</srid>
              <authid>EPSG:4326</authid>
              <description>WGS 84</description>
              <projectionacronym>longlat</projectionacronym>
              <ellipsoidacronym>WGS84</ellipsoidacronym>
              <geographicflag>true</geographicflag>
            </spatialrefsys>
          </srs>
          <provider encoding="UTF-8">postgres</provider>
          <previewExpression>COALESCE( "result_id", '&lt;NULL>' )</previewExpression>
          <vectorjoins/>
          <expressionfields/>
          <map-layer-style-manager current="">
            <map-layer-style name=""/>
          </map-layer-style-manager>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="result_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="view_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="object_type">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="line_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="relation_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="cables">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="wires">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="frequency">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="problem">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
          <renderer-v2 symbollevels="0" type="RuleRenderer">
            <rules key="{d9ac1049-afe9-42b1-92b0-6ead05fdde9c}">
              <rule filter="  &quot;problem&quot; ='dead_end'  " key="{1d1dd98b-15e9-4dad-a1ce-8cae486a5db3}" symbol="0" label="Dead End"/>
              <rule filter=" &quot;problem&quot;  =  'missing_cables' " key="{fc0fc7aa-e6e8-4222-ba6e-678be1d7d26d}" symbol="1" label="Missing Cables"/>
              <rule filter=" &quot;problem&quot;  =  'cable_conflict' " key="{a6456595-dc60-4a50-a8d2-ada7ddf972fa}" symbol="2" label="Cable Conflict"/>
              <rule filter=" &quot;problem&quot;  =  'branch_off_(cables_>_3)' " key="{5a885aab-4d8b-429d-b600-f714a694f50d}" symbol="3" label="Branch Off"/>
              <rule filter=" &quot;problem&quot;  =  'too_many_circuits_on_power_line' " key="{d04c5b53-5f07-493e-b34a-8e7d9d3afb66}" symbol="4" label="Too many Circuits on Power line"/>
              <rule filter=" &quot;problem&quot;  =  'voltage_missing_on_power_line' " key="{635bae8c-6f86-4953-8a63-e33ab94f0e2a}" symbol="5" label="Circuit Voltage missing on Power line"/>
            </rules>
            <symbols>
              <symbol alpha="1" clip_to_extent="1" type="line" name="0">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="31,120,180,255"/>
                  <prop k="line_style" v="dash"/>
                  <prop k="line_width" v="0.4"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="1">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="255,11,60,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="0.4"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="2">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="220,10,196,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="0.4"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="3">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="19,73,110,255"/>
                  <prop k="line_style" v="dot"/>
                  <prop k="line_width" v="0.4"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="4">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="242,229,43,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="0.4"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="5">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="71,163,164,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="0.4"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
            </symbols>
            <effect enabled="0" type="effectStack">
              <effect type="dropShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="outerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
              <effect type="drawSource">
                <prop k="blend_mode" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="1"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
            </effect>
          </renderer-v2>
          <customproperties>
            <property key="labeling" value="pal"/>
            <property key="labeling/addDirectionSymbol" value="false"/>
            <property key="labeling/angleOffset" value="0"/>
            <property key="labeling/blendMode" value="0"/>
            <property key="labeling/bufferBlendMode" value="0"/>
            <property key="labeling/bufferColorA" value="255"/>
            <property key="labeling/bufferColorB" value="255"/>
            <property key="labeling/bufferColorG" value="255"/>
            <property key="labeling/bufferColorR" value="255"/>
            <property key="labeling/bufferDraw" value="false"/>
            <property key="labeling/bufferJoinStyle" value="64"/>
            <property key="labeling/bufferNoFill" value="false"/>
            <property key="labeling/bufferSize" value="1"/>
            <property key="labeling/bufferSizeInMapUnits" value="false"/>
            <property key="labeling/bufferSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/bufferSizeMapUnitMinScale" value="0"/>
            <property key="labeling/bufferTransp" value="0"/>
            <property key="labeling/centroidInside" value="false"/>
            <property key="labeling/centroidWhole" value="false"/>
            <property key="labeling/decimals" value="3"/>
            <property key="labeling/displayAll" value="false"/>
            <property key="labeling/dist" value="0"/>
            <property key="labeling/distInMapUnits" value="false"/>
            <property key="labeling/distMapUnitMaxScale" value="0"/>
            <property key="labeling/distMapUnitMinScale" value="0"/>
            <property key="labeling/enabled" value="false"/>
            <property key="labeling/fieldName" value=""/>
            <property key="labeling/fontBold" value="false"/>
            <property key="labeling/fontCapitals" value="0"/>
            <property key="labeling/fontFamily" value="Lucida Grande"/>
            <property key="labeling/fontItalic" value="false"/>
            <property key="labeling/fontLetterSpacing" value="0"/>
            <property key="labeling/fontLimitPixelSize" value="false"/>
            <property key="labeling/fontMaxPixelSize" value="10000"/>
            <property key="labeling/fontMinPixelSize" value="3"/>
            <property key="labeling/fontSize" value="8.25"/>
            <property key="labeling/fontSizeInMapUnits" value="false"/>
            <property key="labeling/fontSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/fontSizeMapUnitMinScale" value="0"/>
            <property key="labeling/fontStrikeout" value="false"/>
            <property key="labeling/fontUnderline" value="false"/>
            <property key="labeling/fontWeight" value="50"/>
            <property key="labeling/fontWordSpacing" value="0"/>
            <property key="labeling/formatNumbers" value="false"/>
            <property key="labeling/isExpression" value="true"/>
            <property key="labeling/labelOffsetInMapUnits" value="true"/>
            <property key="labeling/labelOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/labelOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/labelPerPart" value="false"/>
            <property key="labeling/leftDirectionSymbol" value="&lt;"/>
            <property key="labeling/limitNumLabels" value="false"/>
            <property key="labeling/maxCurvedCharAngleIn" value="20"/>
            <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
            <property key="labeling/maxNumLabels" value="2000"/>
            <property key="labeling/mergeLines" value="false"/>
            <property key="labeling/minFeatureSize" value="0"/>
            <property key="labeling/multilineAlign" value="0"/>
            <property key="labeling/multilineHeight" value="1"/>
            <property key="labeling/namedStyle" value="Normal"/>
            <property key="labeling/obstacle" value="true"/>
            <property key="labeling/placeDirectionSymbol" value="0"/>
            <property key="labeling/placement" value="2"/>
            <property key="labeling/placementFlags" value="10"/>
            <property key="labeling/plussign" value="false"/>
            <property key="labeling/preserveRotation" value="true"/>
            <property key="labeling/previewBkgrdColor" value="#ffffff"/>
            <property key="labeling/priority" value="5"/>
            <property key="labeling/quadOffset" value="4"/>
            <property key="labeling/repeatDistance" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMaxScale" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMinScale" value="0"/>
            <property key="labeling/repeatDistanceUnit" value="1"/>
            <property key="labeling/reverseDirectionSymbol" value="false"/>
            <property key="labeling/rightDirectionSymbol" value=">"/>
            <property key="labeling/scaleMax" value="10000000"/>
            <property key="labeling/scaleMin" value="1"/>
            <property key="labeling/scaleVisibility" value="false"/>
            <property key="labeling/shadowBlendMode" value="6"/>
            <property key="labeling/shadowColorB" value="0"/>
            <property key="labeling/shadowColorG" value="0"/>
            <property key="labeling/shadowColorR" value="0"/>
            <property key="labeling/shadowDraw" value="false"/>
            <property key="labeling/shadowOffsetAngle" value="135"/>
            <property key="labeling/shadowOffsetDist" value="1"/>
            <property key="labeling/shadowOffsetGlobal" value="true"/>
            <property key="labeling/shadowOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shadowOffsetUnits" value="1"/>
            <property key="labeling/shadowRadius" value="1.5"/>
            <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
            <property key="labeling/shadowRadiusMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowRadiusMapUnitMinScale" value="0"/>
            <property key="labeling/shadowRadiusUnits" value="1"/>
            <property key="labeling/shadowScale" value="100"/>
            <property key="labeling/shadowTransparency" value="30"/>
            <property key="labeling/shadowUnder" value="0"/>
            <property key="labeling/shapeBlendMode" value="0"/>
            <property key="labeling/shapeBorderColorA" value="255"/>
            <property key="labeling/shapeBorderColorB" value="128"/>
            <property key="labeling/shapeBorderColorG" value="128"/>
            <property key="labeling/shapeBorderColorR" value="128"/>
            <property key="labeling/shapeBorderWidth" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMinScale" value="0"/>
            <property key="labeling/shapeBorderWidthUnits" value="1"/>
            <property key="labeling/shapeDraw" value="false"/>
            <property key="labeling/shapeFillColorA" value="255"/>
            <property key="labeling/shapeFillColorB" value="255"/>
            <property key="labeling/shapeFillColorG" value="255"/>
            <property key="labeling/shapeFillColorR" value="255"/>
            <property key="labeling/shapeJoinStyle" value="64"/>
            <property key="labeling/shapeOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shapeOffsetUnits" value="1"/>
            <property key="labeling/shapeOffsetX" value="0"/>
            <property key="labeling/shapeOffsetY" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMinScale" value="0"/>
            <property key="labeling/shapeRadiiUnits" value="1"/>
            <property key="labeling/shapeRadiiX" value="0"/>
            <property key="labeling/shapeRadiiY" value="0"/>
            <property key="labeling/shapeRotation" value="0"/>
            <property key="labeling/shapeRotationType" value="0"/>
            <property key="labeling/shapeSVGFile" value=""/>
            <property key="labeling/shapeSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeSizeMapUnitMinScale" value="0"/>
            <property key="labeling/shapeSizeType" value="0"/>
            <property key="labeling/shapeSizeUnits" value="1"/>
            <property key="labeling/shapeSizeX" value="0"/>
            <property key="labeling/shapeSizeY" value="0"/>
            <property key="labeling/shapeTransparency" value="0"/>
            <property key="labeling/shapeType" value="0"/>
            <property key="labeling/textColorA" value="255"/>
            <property key="labeling/textColorB" value="0"/>
            <property key="labeling/textColorG" value="0"/>
            <property key="labeling/textColorR" value="0"/>
            <property key="labeling/textTransp" value="0"/>
            <property key="labeling/upsidedownLabels" value="0"/>
            <property key="labeling/wrapChar" value=""/>
            <property key="labeling/xOffset" value="0"/>
            <property key="labeling/yOffset" value="0"/>
          </customproperties>
          <blendMode>0</blendMode>
          <featureBlendMode>0</featureBlendMode>
          <layerTransparency>0</layerTransparency>
          <displayfield>line_id</displayfield>
          <label>0</label>
          <labelattributes>
            <label fieldname="" text="Label"/>
            <family fieldname="" name="MS Shell Dlg 2"/>
            <size fieldname="" units="pt" value="12"/>
            <bold fieldname="" on="0"/>
            <italic fieldname="" on="0"/>
            <underline fieldname="" on="0"/>
            <strikeout fieldname="" on="0"/>
            <color fieldname="" red="0" blue="0" green="0"/>
            <x fieldname=""/>
            <y fieldname=""/>
            <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
            <angle fieldname="" value="0" auto="0"/>
            <alignment fieldname="" value="center"/>
            <buffercolor fieldname="" red="255" blue="255" green="255"/>
            <buffersize fieldname="" units="pt" value="1"/>
            <bufferenabled fieldname="" on=""/>
            <multilineenabled fieldname="" on=""/>
            <selectedonly on=""/>
          </labelattributes>
          <SingleCategoryDiagramRenderer diagramType="Pie">
            <DiagramCategory penColor="#000000" labelPlacementMethod="XHeight" penWidth="0" diagramOrientation="Up" minimumSize="0" barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" backgroundColor="#ffffff" transparency="0" width="15" scaleDependency="Area" backgroundAlpha="255" angleOffset="1440" scaleBasedVisibility="0" enabled="0" height="15" sizeType="MM" minScaleDenominator="-4.65661e-10">
              <fontProperties description="Lucida Grande,13,-1,5,50,0,0,0,0,0" style=""/>
              <attribute field="" color="#000000" label=""/>
            </DiagramCategory>
          </SingleCategoryDiagramRenderer>
          <DiagramLayerSettings yPosColumn="-1" linePlacementFlags="10" placement="2" dist="0" xPosColumn="-1" priority="0" obstacle="0" showAll="1"/>
          <editform>.</editform>
          <editforminit/>
          <featformsuppress>0</featformsuppress>
          <annotationform>.</annotationform>
          <editorlayout>generatedlayout</editorlayout>
          <excludeAttributesWMS/>
          <excludeAttributesWFS/>
          <attributeactions/>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="result_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="view_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="object_type">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="line_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="relation_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="cables">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="wires">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="frequency">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="problem">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
        </maplayer>
        <maplayer minimumScale="0" maximumScale="587421" simplifyDrawingHints="1" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" geometry="Polygon" simplifyMaxScale="1" type="vector" hasScaleBasedVisibilityFlag="1" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
          <id>view_substations20151217121906140</id>
          <datasource>dbname='"""+database+"""' host="""+host+""" port="""+port+""" user='"""+user+"""' password='"""+password+"""' sslmode=disable key='view_id' srid=4326 type=Polygon table="results"."view_substations" (geom) sql=</datasource>
          <title></title>
          <abstract></abstract>
          <keywordList>
            <value></value>
          </keywordList>
          <layername>view_substations</layername>
          <srs>
            <spatialrefsys>
              <proj4>+proj=longlat +datum=WGS84 +no_defs</proj4>
              <srsid>3452</srsid>
              <srid>4326</srid>
              <authid>EPSG:4326</authid>
              <description>WGS 84</description>
              <projectionacronym>longlat</projectionacronym>
              <ellipsoidacronym>WGS84</ellipsoidacronym>
              <geographicflag>true</geographicflag>
            </spatialrefsys>
          </srs>
          <provider encoding="UTF-8">postgres</provider>
          <previewExpression></previewExpression>
          <vectorjoins/>
          <expressionfields/>
          <map-layer-style-manager current="">
            <map-layer-style name=""/>
          </map-layer-style-manager>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="result_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="view_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="osm_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="s_long">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="name">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="center_geom">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
          <renderer-v2 symbollevels="0" type="singleSymbol">
            <symbols>
              <symbol alpha="1" clip_to_extent="1" type="fill" name="0">
                <layer pass="0" class="SimpleFill" locked="0">
                  <prop k="border_width_map_unit_scale" v="0,0"/>
                  <prop k="color" v="31,120,180,255"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="0,0,0,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0.26"/>
                  <prop k="outline_width_unit" v="MM"/>
                  <prop k="style" v="solid"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
            </symbols>
            <rotation/>
            <sizescale scalemethod="diameter"/>
            <effect enabled="0" type="effectStack">
              <effect type="dropShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="outerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
              <effect type="drawSource">
                <prop k="blend_mode" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="1"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
            </effect>
          </renderer-v2>
          <customproperties>
            <property key="labeling" value="pal"/>
            <property key="labeling/addDirectionSymbol" value="false"/>
            <property key="labeling/angleOffset" value="0"/>
            <property key="labeling/blendMode" value="0"/>
            <property key="labeling/bufferBlendMode" value="0"/>
            <property key="labeling/bufferColorA" value="255"/>
            <property key="labeling/bufferColorB" value="255"/>
            <property key="labeling/bufferColorG" value="255"/>
            <property key="labeling/bufferColorR" value="255"/>
            <property key="labeling/bufferDraw" value="true"/>
            <property key="labeling/bufferJoinStyle" value="64"/>
            <property key="labeling/bufferNoFill" value="false"/>
            <property key="labeling/bufferSize" value="1"/>
            <property key="labeling/bufferSizeInMapUnits" value="false"/>
            <property key="labeling/bufferSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/bufferSizeMapUnitMinScale" value="0"/>
            <property key="labeling/bufferTransp" value="0"/>
            <property key="labeling/centroidInside" value="false"/>
            <property key="labeling/centroidWhole" value="false"/>
            <property key="labeling/decimals" value="3"/>
            <property key="labeling/displayAll" value="false"/>
            <property key="labeling/dist" value="0"/>
            <property key="labeling/distInMapUnits" value="false"/>
            <property key="labeling/distMapUnitMaxScale" value="0"/>
            <property key="labeling/distMapUnitMinScale" value="0"/>
            <property key="labeling/enabled" value="true"/>
            <property key="labeling/fieldName" value="name"/>
            <property key="labeling/fontBold" value="false"/>
            <property key="labeling/fontCapitals" value="0"/>
            <property key="labeling/fontFamily" value="Lucida Grande"/>
            <property key="labeling/fontItalic" value="false"/>
            <property key="labeling/fontLetterSpacing" value="0"/>
            <property key="labeling/fontLimitPixelSize" value="false"/>
            <property key="labeling/fontMaxPixelSize" value="10000"/>
            <property key="labeling/fontMinPixelSize" value="3"/>
            <property key="labeling/fontSize" value="9.25"/>
            <property key="labeling/fontSizeInMapUnits" value="false"/>
            <property key="labeling/fontSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/fontSizeMapUnitMinScale" value="0"/>
            <property key="labeling/fontStrikeout" value="false"/>
            <property key="labeling/fontUnderline" value="false"/>
            <property key="labeling/fontWeight" value="50"/>
            <property key="labeling/fontWordSpacing" value="0"/>
            <property key="labeling/formatNumbers" value="false"/>
            <property key="labeling/isExpression" value="false"/>
            <property key="labeling/labelOffsetInMapUnits" value="true"/>
            <property key="labeling/labelOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/labelOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/labelPerPart" value="false"/>
            <property key="labeling/leftDirectionSymbol" value="&lt;"/>
            <property key="labeling/limitNumLabels" value="false"/>
            <property key="labeling/maxCurvedCharAngleIn" value="20"/>
            <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
            <property key="labeling/maxNumLabels" value="2000"/>
            <property key="labeling/mergeLines" value="false"/>
            <property key="labeling/minFeatureSize" value="0"/>
            <property key="labeling/multilineAlign" value="0"/>
            <property key="labeling/multilineHeight" value="1"/>
            <property key="labeling/namedStyle" value="Normal"/>
            <property key="labeling/obstacle" value="true"/>
            <property key="labeling/placeDirectionSymbol" value="0"/>
            <property key="labeling/placement" value="1"/>
            <property key="labeling/placementFlags" value="0"/>
            <property key="labeling/plussign" value="false"/>
            <property key="labeling/preserveRotation" value="true"/>
            <property key="labeling/previewBkgrdColor" value="#ffffff"/>
            <property key="labeling/priority" value="5"/>
            <property key="labeling/quadOffset" value="2"/>
            <property key="labeling/repeatDistance" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMaxScale" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMinScale" value="0"/>
            <property key="labeling/repeatDistanceUnit" value="1"/>
            <property key="labeling/reverseDirectionSymbol" value="false"/>
            <property key="labeling/rightDirectionSymbol" value=">"/>
            <property key="labeling/scaleMax" value="10000000"/>
            <property key="labeling/scaleMin" value="1"/>
            <property key="labeling/scaleVisibility" value="false"/>
            <property key="labeling/shadowBlendMode" value="6"/>
            <property key="labeling/shadowColorB" value="0"/>
            <property key="labeling/shadowColorG" value="0"/>
            <property key="labeling/shadowColorR" value="0"/>
            <property key="labeling/shadowDraw" value="false"/>
            <property key="labeling/shadowOffsetAngle" value="135"/>
            <property key="labeling/shadowOffsetDist" value="1"/>
            <property key="labeling/shadowOffsetGlobal" value="true"/>
            <property key="labeling/shadowOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shadowOffsetUnits" value="1"/>
            <property key="labeling/shadowRadius" value="1.5"/>
            <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
            <property key="labeling/shadowRadiusMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowRadiusMapUnitMinScale" value="0"/>
            <property key="labeling/shadowRadiusUnits" value="1"/>
            <property key="labeling/shadowScale" value="100"/>
            <property key="labeling/shadowTransparency" value="30"/>
            <property key="labeling/shadowUnder" value="0"/>
            <property key="labeling/shapeBlendMode" value="0"/>
            <property key="labeling/shapeBorderColorA" value="255"/>
            <property key="labeling/shapeBorderColorB" value="128"/>
            <property key="labeling/shapeBorderColorG" value="128"/>
            <property key="labeling/shapeBorderColorR" value="128"/>
            <property key="labeling/shapeBorderWidth" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMinScale" value="0"/>
            <property key="labeling/shapeBorderWidthUnits" value="1"/>
            <property key="labeling/shapeDraw" value="false"/>
            <property key="labeling/shapeFillColorA" value="255"/>
            <property key="labeling/shapeFillColorB" value="255"/>
            <property key="labeling/shapeFillColorG" value="255"/>
            <property key="labeling/shapeFillColorR" value="255"/>
            <property key="labeling/shapeJoinStyle" value="64"/>
            <property key="labeling/shapeOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shapeOffsetUnits" value="1"/>
            <property key="labeling/shapeOffsetX" value="0"/>
            <property key="labeling/shapeOffsetY" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMinScale" value="0"/>
            <property key="labeling/shapeRadiiUnits" value="1"/>
            <property key="labeling/shapeRadiiX" value="0"/>
            <property key="labeling/shapeRadiiY" value="0"/>
            <property key="labeling/shapeRotation" value="0"/>
            <property key="labeling/shapeRotationType" value="0"/>
            <property key="labeling/shapeSVGFile" value=""/>
            <property key="labeling/shapeSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeSizeMapUnitMinScale" value="0"/>
            <property key="labeling/shapeSizeType" value="0"/>
            <property key="labeling/shapeSizeUnits" value="1"/>
            <property key="labeling/shapeSizeX" value="0"/>
            <property key="labeling/shapeSizeY" value="0"/>
            <property key="labeling/shapeTransparency" value="0"/>
            <property key="labeling/shapeType" value="0"/>
            <property key="labeling/textColorA" value="255"/>
            <property key="labeling/textColorB" value="0"/>
            <property key="labeling/textColorG" value="0"/>
            <property key="labeling/textColorR" value="0"/>
            <property key="labeling/textTransp" value="0"/>
            <property key="labeling/upsidedownLabels" value="0"/>
            <property key="labeling/wrapChar" value=""/>
            <property key="labeling/xOffset" value="0"/>
            <property key="labeling/yOffset" value="0"/>
          </customproperties>
          <blendMode>0</blendMode>
          <featureBlendMode>0</featureBlendMode>
          <layerTransparency>75</layerTransparency>
          <displayfield>id</displayfield>
          <label>0</label>
          <labelattributes>
            <label fieldname="" text="Label"/>
            <family fieldname="" name="MS Shell Dlg 2"/>
            <size fieldname="" units="pt" value="12"/>
            <bold fieldname="" on="0"/>
            <italic fieldname="" on="0"/>
            <underline fieldname="" on="0"/>
            <strikeout fieldname="" on="0"/>
            <color fieldname="" red="0" blue="0" green="0"/>
            <x fieldname=""/>
            <y fieldname=""/>
            <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
            <angle fieldname="" value="0" auto="0"/>
            <alignment fieldname="" value="center"/>
            <buffercolor fieldname="" red="255" blue="255" green="255"/>
            <buffersize fieldname="" units="pt" value="1"/>
            <bufferenabled fieldname="" on=""/>
            <multilineenabled fieldname="" on=""/>
            <selectedonly on=""/>
          </labelattributes>
          <SingleCategoryDiagramRenderer diagramType="Pie">
            <DiagramCategory penColor="#000000" labelPlacementMethod="XHeight" penWidth="0" diagramOrientation="Up" minimumSize="0" barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" backgroundColor="#ffffff" transparency="0" width="15" scaleDependency="Area" backgroundAlpha="255" angleOffset="1440" scaleBasedVisibility="0" enabled="0" height="15" sizeType="MM" minScaleDenominator="-4.65661e-10">
              <fontProperties description="Lucida Grande,13,-1,5,50,0,0,0,0,0" style=""/>
              <attribute field="" color="#000000" label=""/>
            </DiagramCategory>
          </SingleCategoryDiagramRenderer>
          <DiagramLayerSettings yPosColumn="-1" linePlacementFlags="10" placement="0" dist="0" xPosColumn="-1" priority="0" obstacle="0" showAll="1"/>
          <editform>.</editform>
          <editforminit/>
          <featformsuppress>0</featformsuppress>
          <annotationform>.</annotationform>
          <editorlayout>generatedlayout</editorlayout>
          <excludeAttributesWMS/>
          <excludeAttributesWFS/>
          <attributeactions/>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="result_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="view_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="osm_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="s_long">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="name">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="center_geom">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
        </maplayer>
      </projectlayers>
      <properties>
        <SpatialRefSys>
          <ProjectCRSProj4String type="QString">+proj=longlat +datum=WGS84 +no_defs</ProjectCRSProj4String>
          <ProjectCrs type="QString">EPSG:4326</ProjectCrs>
          <ProjectCRSID type="int">3452</ProjectCRSID>
          <ProjectionsEnabled type="int">0</ProjectionsEnabled>
        </SpatialRefSys>
        <Paths>
          <Absolute type="bool">false</Absolute>
        </Paths>
        <Gui>
          <SelectionColorBluePart type="int">0</SelectionColorBluePart>
          <CanvasColorGreenPart type="int">255</CanvasColorGreenPart>
          <CanvasColorRedPart type="int">255</CanvasColorRedPart>
          <SelectionColorRedPart type="int">255</SelectionColorRedPart>
          <SelectionColorAlphaPart type="int">255</SelectionColorAlphaPart>
          <SelectionColorGreenPart type="int">255</SelectionColorGreenPart>
          <CanvasColorBluePart type="int">255</CanvasColorBluePart>
        </Gui>
        <Digitizing>
          <DefaultSnapToleranceUnit type="int">2</DefaultSnapToleranceUnit>
          <LayerSnappingList type="QStringList">
            <value>view_branch_data20151217133637741</value>
            <value>view_bus_data20151217121906009</value>
            <value>view_dcline_data20151217133332218</value>
            <value>view_problem_log20151217121906087</value>
            <value>view_substations20151217121906140</value>
          </LayerSnappingList>
          <LayerSnappingEnabledList type="QStringList">
            <value>disabled</value>
            <value>disabled</value>
            <value>disabled</value>
            <value>disabled</value>
            <value>disabled</value>
          </LayerSnappingEnabledList>
          <SnappingMode type="QString">current_layer</SnappingMode>
          <AvoidIntersectionsList type="QStringList"/>
          <LayerSnappingToleranceUnitList type="QStringList">
            <value>2</value>
            <value>2</value>
            <value>2</value>
            <value>2</value>
            <value>2</value>
          </LayerSnappingToleranceUnitList>
          <LayerSnapToList type="QStringList">
            <value>to_vertex_and_segment</value>
            <value>to_vertex_and_segment</value>
            <value>to_vertex_and_segment</value>
            <value>to_vertex_and_segment</value>
            <value>to_vertex_and_segment</value>
          </LayerSnapToList>
          <DefaultSnapType type="QString">off</DefaultSnapType>
          <DefaultSnapTolerance type="double">0</DefaultSnapTolerance>
          <LayerSnappingToleranceList type="QStringList">
            <value>0.000000</value>
            <value>0.000000</value>
            <value>0.000000</value>
            <value>0.000000</value>
            <value>0.000000</value>
          </LayerSnappingToleranceList>
        </Digitizing>
        <PositionPrecision>
          <DecimalPlaces type="int">2</DecimalPlaces>
          <Automatic type="bool">true</Automatic>
        </PositionPrecision>
        <Legend>
          <filterByMap type="bool">false</filterByMap>
        </Legend>
      </properties>
    </qgis>
    """

    filepath = qgis_proj_dir + "/"+ database + "_results_project.qgs"

    if os.path.exists(filepath) == False:
        fh = open(filepath ,"w")
        fh.write(result_project)
        fh.close()


    grid_devel_project = """

        <!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
    <qgis projectname="" version="2.10.1-Pisa">
      <title></title>
      <layer-tree-group expanded="1" checked="Qt::Checked" name="">
        <customproperties/>
        <layer-tree-layer expanded="1" checked="Qt::Checked" id="vw_change_log20151204114804760" name="vw_change_log">
          <customproperties/>
        </layer-tree-layer>
        <layer-tree-layer expanded="1" checked="Qt::Checked" id="edit_power_relations20151214185446433" name="edit_power_relations">
          <customproperties/>
        </layer-tree-layer>
        <layer-tree-layer expanded="1" checked="Qt::Checked" id="power_ways20151204114804618" name="power_ways">
          <customproperties/>
        </layer-tree-layer>
      </layer-tree-group>
      <relations/>
      <mapcanvas>
        <units>degrees</units>
        <extent>
          <xmin>5.9040642516733417</xmin>
          <ymin>48.85804593092658621</ymin>
          <xmax>12.8416930407427099</xmax>
          <ymax>53.67844787833390541</ymax>
        </extent>
        <rotation>0</rotation>
        <projections>1</projections>
        <destinationsrs>
          <spatialrefsys>
            <proj4>+proj=longlat +datum=WGS84 +no_defs</proj4>
            <srsid>3452</srsid>
            <srid>4326</srid>
            <authid>EPSG:4326</authid>
            <description>WGS 84</description>
            <projectionacronym>longlat</projectionacronym>
            <ellipsoidacronym>WGS84</ellipsoidacronym>
            <geographicflag>true</geographicflag>
          </spatialrefsys>
        </destinationsrs>
        <layer_coordinate_transform_info>
          <layer_coordinate_transform destAuthId="EPSG:4326" srcAuthId="EPSG:4326" srcDatumTransform="-1" destDatumTransform="-1" layerid="edit_power_relations20151214185446433"/>
          <layer_coordinate_transform destAuthId="EPSG:4326" srcAuthId="EPSG:4326" srcDatumTransform="-1" destDatumTransform="-1" layerid="vw_change_log20151204114804760"/>
          <layer_coordinate_transform destAuthId="EPSG:4326" srcAuthId="EPSG:4326" srcDatumTransform="-1" destDatumTransform="-1" layerid="power_ways20151204114804618"/>
        </layer_coordinate_transform_info>
      </mapcanvas>
      <visibility-presets/>
      <layer-tree-canvas>
        <custom-order enabled="0">
          <item>power_ways20151204114804618</item>
          <item>vw_change_log20151204114804760</item>
          <item>edit_power_relations20151214185446433</item>
        </custom-order>
      </layer-tree-canvas>
      <legend updateDrawingOrder="true">
        <legendlayer drawingOrder="-1" open="true" checked="Qt::Checked" name="vw_change_log" showFeatureCount="0">
          <filegroup open="true" hidden="false">
            <legendlayerfile isInOverview="0" layerid="vw_change_log20151204114804760" visible="1"/>
          </filegroup>
        </legendlayer>
        <legendlayer drawingOrder="-1" open="true" checked="Qt::Checked" name="edit_power_relations" showFeatureCount="0">
          <filegroup open="true" hidden="false">
            <legendlayerfile isInOverview="0" layerid="edit_power_relations20151214185446433" visible="1"/>
          </filegroup>
        </legendlayer>
        <legendlayer drawingOrder="-1" open="true" checked="Qt::Checked" name="power_ways" showFeatureCount="0">
          <filegroup open="true" hidden="false">
            <legendlayerfile isInOverview="0" layerid="power_ways20151204114804618" visible="1"/>
          </filegroup>
        </legendlayer>
      </legend>
      <projectlayers layercount="3">
        <maplayer minimumScale="0" maximumScale="1e+08" simplifyDrawingHints="1" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" geometry="Line" simplifyMaxScale="1" type="vector" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
          <id>edit_power_relations20151214185446433</id>
          <datasource>dbname='"""+database+"""' host="""+host+""" port="""+port+""" user='"""+user+"""' password='"""+password+"""' sslmode=disable key='id' srid=4326 type=MultiLineString table="public"."edit_power_relations" (st_union) sql=</datasource>
          <title></title>
          <abstract></abstract>
          <keywordList>
            <value></value>
          </keywordList>
          <layername>edit_power_relations</layername>
          <srs>
            <spatialrefsys>
              <proj4>+proj=longlat +datum=WGS84 +no_defs</proj4>
              <srsid>3452</srsid>
              <srid>4326</srid>
              <authid>EPSG:4326</authid>
              <description>WGS 84</description>
              <projectionacronym>longlat</projectionacronym>
              <ellipsoidacronym>WGS84</ellipsoidacronym>
              <geographicflag>true</geographicflag>
            </spatialrefsys>
          </srs>
          <provider encoding="UTF-8">postgres</provider>
          <previewExpression></previewExpression>
          <vectorjoins/>
          <expressionfields/>
          <map-layer-style-manager current="">
            <map-layer-style name=""/>
          </map-layer-style-manager>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="cables">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="wires">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="circuits">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="frequency">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="members">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
          <renderer-v2 symbollevels="0" type="RuleRenderer">
            <rules key="{148bb227-0993-4418-b3eb-af4ec6ac338b}">
              <rule checkstate="0" key="{9909ee22-99c8-4bb8-8ee0-05535a899654}" symbol="0" label="All"/>
              <rule filter=" &quot;voltage&quot;  = 220000 OR  &quot;voltage&quot;  = 380000" key="{648e9ac3-061e-433f-b400-b3b12b80ea93}" symbol="1" label="220kV, 380kV"/>
            </rules>
            <symbols>
              <symbol alpha="0.286275" clip_to_extent="1" type="line" name="0">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="0,0,0,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="0.09"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="0.835294" clip_to_extent="1" type="line" name="1">
                <layer pass="1" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="0,0,0,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="0.18"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="5.55112e-17"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
            </symbols>
            <effect enabled="0" type="effectStack">
              <effect type="dropShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="outerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
              <effect type="drawSource">
                <prop k="blend_mode" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="1"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
            </effect>
          </renderer-v2>
          <customproperties>
            <property key="labeling" value="pal"/>
            <property key="labeling/addDirectionSymbol" value="false"/>
            <property key="labeling/angleOffset" value="0"/>
            <property key="labeling/blendMode" value="0"/>
            <property key="labeling/bufferBlendMode" value="0"/>
            <property key="labeling/bufferColorA" value="255"/>
            <property key="labeling/bufferColorB" value="255"/>
            <property key="labeling/bufferColorG" value="255"/>
            <property key="labeling/bufferColorR" value="255"/>
            <property key="labeling/bufferDraw" value="false"/>
            <property key="labeling/bufferJoinStyle" value="64"/>
            <property key="labeling/bufferNoFill" value="false"/>
            <property key="labeling/bufferSize" value="1"/>
            <property key="labeling/bufferSizeInMapUnits" value="false"/>
            <property key="labeling/bufferSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/bufferSizeMapUnitMinScale" value="0"/>
            <property key="labeling/bufferTransp" value="0"/>
            <property key="labeling/centroidInside" value="false"/>
            <property key="labeling/centroidWhole" value="false"/>
            <property key="labeling/decimals" value="3"/>
            <property key="labeling/displayAll" value="false"/>
            <property key="labeling/dist" value="0"/>
            <property key="labeling/distInMapUnits" value="false"/>
            <property key="labeling/distMapUnitMaxScale" value="0"/>
            <property key="labeling/distMapUnitMinScale" value="0"/>
            <property key="labeling/enabled" value="false"/>
            <property key="labeling/fieldName" value=""/>
            <property key="labeling/fontBold" value="false"/>
            <property key="labeling/fontCapitals" value="0"/>
            <property key="labeling/fontFamily" value="Lucida Grande"/>
            <property key="labeling/fontItalic" value="false"/>
            <property key="labeling/fontLetterSpacing" value="0"/>
            <property key="labeling/fontLimitPixelSize" value="false"/>
            <property key="labeling/fontMaxPixelSize" value="10000"/>
            <property key="labeling/fontMinPixelSize" value="3"/>
            <property key="labeling/fontSize" value="8.25"/>
            <property key="labeling/fontSizeInMapUnits" value="false"/>
            <property key="labeling/fontSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/fontSizeMapUnitMinScale" value="0"/>
            <property key="labeling/fontStrikeout" value="false"/>
            <property key="labeling/fontUnderline" value="false"/>
            <property key="labeling/fontWeight" value="50"/>
            <property key="labeling/fontWordSpacing" value="0"/>
            <property key="labeling/formatNumbers" value="false"/>
            <property key="labeling/isExpression" value="true"/>
            <property key="labeling/labelOffsetInMapUnits" value="true"/>
            <property key="labeling/labelOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/labelOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/labelPerPart" value="false"/>
            <property key="labeling/leftDirectionSymbol" value="&lt;"/>
            <property key="labeling/limitNumLabels" value="false"/>
            <property key="labeling/maxCurvedCharAngleIn" value="20"/>
            <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
            <property key="labeling/maxNumLabels" value="2000"/>
            <property key="labeling/mergeLines" value="false"/>
            <property key="labeling/minFeatureSize" value="0"/>
            <property key="labeling/multilineAlign" value="0"/>
            <property key="labeling/multilineHeight" value="1"/>
            <property key="labeling/namedStyle" value="Normal"/>
            <property key="labeling/obstacle" value="true"/>
            <property key="labeling/placeDirectionSymbol" value="0"/>
            <property key="labeling/placement" value="2"/>
            <property key="labeling/placementFlags" value="10"/>
            <property key="labeling/plussign" value="false"/>
            <property key="labeling/preserveRotation" value="true"/>
            <property key="labeling/previewBkgrdColor" value="#ffffff"/>
            <property key="labeling/priority" value="5"/>
            <property key="labeling/quadOffset" value="4"/>
            <property key="labeling/repeatDistance" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMaxScale" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMinScale" value="0"/>
            <property key="labeling/repeatDistanceUnit" value="1"/>
            <property key="labeling/reverseDirectionSymbol" value="false"/>
            <property key="labeling/rightDirectionSymbol" value=">"/>
            <property key="labeling/scaleMax" value="10000000"/>
            <property key="labeling/scaleMin" value="1"/>
            <property key="labeling/scaleVisibility" value="false"/>
            <property key="labeling/shadowBlendMode" value="6"/>
            <property key="labeling/shadowColorB" value="0"/>
            <property key="labeling/shadowColorG" value="0"/>
            <property key="labeling/shadowColorR" value="0"/>
            <property key="labeling/shadowDraw" value="false"/>
            <property key="labeling/shadowOffsetAngle" value="135"/>
            <property key="labeling/shadowOffsetDist" value="1"/>
            <property key="labeling/shadowOffsetGlobal" value="true"/>
            <property key="labeling/shadowOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shadowOffsetUnits" value="1"/>
            <property key="labeling/shadowRadius" value="1.5"/>
            <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
            <property key="labeling/shadowRadiusMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowRadiusMapUnitMinScale" value="0"/>
            <property key="labeling/shadowRadiusUnits" value="1"/>
            <property key="labeling/shadowScale" value="100"/>
            <property key="labeling/shadowTransparency" value="30"/>
            <property key="labeling/shadowUnder" value="0"/>
            <property key="labeling/shapeBlendMode" value="0"/>
            <property key="labeling/shapeBorderColorA" value="255"/>
            <property key="labeling/shapeBorderColorB" value="128"/>
            <property key="labeling/shapeBorderColorG" value="128"/>
            <property key="labeling/shapeBorderColorR" value="128"/>
            <property key="labeling/shapeBorderWidth" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMinScale" value="0"/>
            <property key="labeling/shapeBorderWidthUnits" value="1"/>
            <property key="labeling/shapeDraw" value="false"/>
            <property key="labeling/shapeFillColorA" value="255"/>
            <property key="labeling/shapeFillColorB" value="255"/>
            <property key="labeling/shapeFillColorG" value="255"/>
            <property key="labeling/shapeFillColorR" value="255"/>
            <property key="labeling/shapeJoinStyle" value="64"/>
            <property key="labeling/shapeOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shapeOffsetUnits" value="1"/>
            <property key="labeling/shapeOffsetX" value="0"/>
            <property key="labeling/shapeOffsetY" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMinScale" value="0"/>
            <property key="labeling/shapeRadiiUnits" value="1"/>
            <property key="labeling/shapeRadiiX" value="0"/>
            <property key="labeling/shapeRadiiY" value="0"/>
            <property key="labeling/shapeRotation" value="0"/>
            <property key="labeling/shapeRotationType" value="0"/>
            <property key="labeling/shapeSVGFile" value=""/>
            <property key="labeling/shapeSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeSizeMapUnitMinScale" value="0"/>
            <property key="labeling/shapeSizeType" value="0"/>
            <property key="labeling/shapeSizeUnits" value="1"/>
            <property key="labeling/shapeSizeX" value="0"/>
            <property key="labeling/shapeSizeY" value="0"/>
            <property key="labeling/shapeTransparency" value="0"/>
            <property key="labeling/shapeType" value="0"/>
            <property key="labeling/textColorA" value="255"/>
            <property key="labeling/textColorB" value="0"/>
            <property key="labeling/textColorG" value="0"/>
            <property key="labeling/textColorR" value="0"/>
            <property key="labeling/textTransp" value="0"/>
            <property key="labeling/upsidedownLabels" value="0"/>
            <property key="labeling/wrapChar" value=""/>
            <property key="labeling/xOffset" value="0"/>
            <property key="labeling/yOffset" value="0"/>
          </customproperties>
          <blendMode>0</blendMode>
          <featureBlendMode>0</featureBlendMode>
          <layerTransparency>0</layerTransparency>
          <displayfield>id</displayfield>
          <label>0</label>
          <labelattributes>
            <label fieldname="" text="Beschriftung"/>
            <family fieldname="" name="MS Shell Dlg 2"/>
            <size fieldname="" units="pt" value="12"/>
            <bold fieldname="" on="0"/>
            <italic fieldname="" on="0"/>
            <underline fieldname="" on="0"/>
            <strikeout fieldname="" on="0"/>
            <color fieldname="" red="0" blue="0" green="0"/>
            <x fieldname=""/>
            <y fieldname=""/>
            <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
            <angle fieldname="" value="0" auto="0"/>
            <alignment fieldname="" value="center"/>
            <buffercolor fieldname="" red="255" blue="255" green="255"/>
            <buffersize fieldname="" units="pt" value="1"/>
            <bufferenabled fieldname="" on=""/>
            <multilineenabled fieldname="" on=""/>
            <selectedonly on=""/>
          </labelattributes>
          <SingleCategoryDiagramRenderer diagramType="Pie">
            <DiagramCategory penColor="#000000" labelPlacementMethod="XHeight" penWidth="0" diagramOrientation="Up" minimumSize="0" barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" backgroundColor="#ffffff" transparency="0" width="15" scaleDependency="Area" backgroundAlpha="255" angleOffset="1440" scaleBasedVisibility="0" enabled="0" height="15" sizeType="MM" minScaleDenominator="-4.65661e-10">
              <fontProperties description="Lucida Grande,13,-1,5,50,0,0,0,0,0" style=""/>
              <attribute field="" color="#000000" label=""/>
            </DiagramCategory>
          </SingleCategoryDiagramRenderer>
          <DiagramLayerSettings yPosColumn="-1" linePlacementFlags="10" placement="2" dist="0" xPosColumn="-1" priority="0" obstacle="0" showAll="1"/>
          <editform>.</editform>
          <editforminit/>
          <featformsuppress>0</featformsuppress>
          <annotationform>.</annotationform>
          <editorlayout>generatedlayout</editorlayout>
          <excludeAttributesWMS/>
          <excludeAttributesWFS/>
          <attributeactions/>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="cables">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="wires">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="circuits">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="frequency">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="members">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
        </maplayer>
        <maplayer minimumScale="0" maximumScale="1e+08" simplifyDrawingHints="1" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" geometry="Line" simplifyMaxScale="1" type="vector" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
          <id>power_ways20151204114804618</id>
          <datasource>dbname='"""+database+"""' host="""+host+""" port="""+port+""" user='"""+user+"""' password='"""+password+"""' sslmode=disable key='id' srid=4326 type=LineString table="public"."power_ways" (way) sql=</datasource>
          <title></title>
          <abstract></abstract>
          <keywordList>
            <value></value>
          </keywordList>
          <layername>power_ways</layername>
          <srs>
            <spatialrefsys>
              <proj4>+proj=longlat +datum=WGS84 +no_defs</proj4>
              <srsid>3452</srsid>
              <srid>4326</srid>
              <authid>EPSG:4326</authid>
              <description>WGS 84</description>
              <projectionacronym>longlat</projectionacronym>
              <ellipsoidacronym>WGS84</ellipsoidacronym>
              <geographicflag>true</geographicflag>
            </spatialrefsys>
          </srs>
          <provider encoding="UTF-8">postgres</provider>
          <previewExpression>COALESCE( "id", '&lt;NULL>' )</previewExpression>
          <vectorjoins/>
          <expressionfields/>
          <map-layer-style-manager current="">
            <map-layer-style name=""/>
          </map-layer-style-manager>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="id">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="version">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="user_id">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="tstamp">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="changeset_id">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="UniqueValues" name="power">
              <widgetv2config fieldEditable="1" labelOnTop="0" Editable="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="cables">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="wires">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="circuits">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="frequency">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="name">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
          <renderer-v2 symbollevels="0" type="RuleRenderer">
            <rules key="{dc76d4cb-b494-4520-b47b-ee6d7ca9b438}">
              <rule filter="( &quot;voltage&quot;  ILIKE '%380000%' OR  &quot;voltage&quot;  ILIKE '%220000%') AND power = 'line'" key="{966cb1d8-8143-4d23-be19-610aba027c2d}" symbol="0" label="> 220 kV (line)"/>
              <rule filter="&quot;power&quot; = 'substation'" key="{555cb5d4-8e5d-447c-909c-ec72064c7ff8}" symbol="1" label="Substations"/>
              <rule key="{eee7601b-e532-4b27-ad40-ab317567e1f4}" symbol="2" label="All"/>
            </rules>
            <symbols>
              <symbol alpha="1" clip_to_extent="1" type="line" name="0">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="157,157,157,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="1.46"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="1">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="0,0,0,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="0.26"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="0.321569" clip_to_extent="1" type="line" name="2">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="157,157,157,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="0.46"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
            </symbols>
            <effect enabled="0" type="effectStack">
              <effect type="dropShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="outerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
              <effect type="drawSource">
                <prop k="blend_mode" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="1"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
            </effect>
          </renderer-v2>
          <customproperties>
            <property key="labeling" value="pal"/>
            <property key="labeling/addDirectionSymbol" value="false"/>
            <property key="labeling/angleOffset" value="0"/>
            <property key="labeling/blendMode" value="0"/>
            <property key="labeling/bufferBlendMode" value="0"/>
            <property key="labeling/bufferColorA" value="255"/>
            <property key="labeling/bufferColorB" value="255"/>
            <property key="labeling/bufferColorG" value="255"/>
            <property key="labeling/bufferColorR" value="255"/>
            <property key="labeling/bufferDraw" value="false"/>
            <property key="labeling/bufferJoinStyle" value="64"/>
            <property key="labeling/bufferNoFill" value="false"/>
            <property key="labeling/bufferSize" value="1"/>
            <property key="labeling/bufferSizeInMapUnits" value="false"/>
            <property key="labeling/bufferSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/bufferSizeMapUnitMinScale" value="0"/>
            <property key="labeling/bufferTransp" value="0"/>
            <property key="labeling/centroidInside" value="false"/>
            <property key="labeling/centroidWhole" value="false"/>
            <property key="labeling/dataDefined/AlwaysShow" value="0~~0~~CASE WHEN (power='substation' or power = 'sub_station') THEN name END~~name"/>
            <property key="labeling/dataDefined/Show" value="0~~0~~~~name"/>
            <property key="labeling/decimals" value="3"/>
            <property key="labeling/displayAll" value="true"/>
            <property key="labeling/dist" value="0"/>
            <property key="labeling/distInMapUnits" value="false"/>
            <property key="labeling/distMapUnitMaxScale" value="0"/>
            <property key="labeling/distMapUnitMinScale" value="0"/>
            <property key="labeling/enabled" value="true"/>
            <property key="labeling/fieldName" value="CASE WHEN (power='substation' or power = 'sub_station') AND (voltage iLIKE '%380%' or voltage iLike '%220%')THEN name END"/>
            <property key="labeling/fontBold" value="false"/>
            <property key="labeling/fontCapitals" value="0"/>
            <property key="labeling/fontFamily" value="Lucida Grande"/>
            <property key="labeling/fontItalic" value="false"/>
            <property key="labeling/fontLetterSpacing" value="0"/>
            <property key="labeling/fontLimitPixelSize" value="false"/>
            <property key="labeling/fontMaxPixelSize" value="10000"/>
            <property key="labeling/fontMinPixelSize" value="3"/>
            <property key="labeling/fontSize" value="10.25"/>
            <property key="labeling/fontSizeInMapUnits" value="false"/>
            <property key="labeling/fontSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/fontSizeMapUnitMinScale" value="0"/>
            <property key="labeling/fontStrikeout" value="false"/>
            <property key="labeling/fontUnderline" value="false"/>
            <property key="labeling/fontWeight" value="50"/>
            <property key="labeling/fontWordSpacing" value="0"/>
            <property key="labeling/formatNumbers" value="false"/>
            <property key="labeling/isExpression" value="true"/>
            <property key="labeling/labelOffsetInMapUnits" value="true"/>
            <property key="labeling/labelOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/labelOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/labelPerPart" value="true"/>
            <property key="labeling/leftDirectionSymbol" value="&lt;"/>
            <property key="labeling/limitNumLabels" value="false"/>
            <property key="labeling/maxCurvedCharAngleIn" value="20"/>
            <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
            <property key="labeling/maxNumLabels" value="2000"/>
            <property key="labeling/mergeLines" value="false"/>
            <property key="labeling/minFeatureSize" value="0"/>
            <property key="labeling/multilineAlign" value="0"/>
            <property key="labeling/multilineHeight" value="1"/>
            <property key="labeling/namedStyle" value="Normal"/>
            <property key="labeling/obstacle" value="false"/>
            <property key="labeling/placeDirectionSymbol" value="0"/>
            <property key="labeling/placement" value="4"/>
            <property key="labeling/placementFlags" value="0"/>
            <property key="labeling/plussign" value="false"/>
            <property key="labeling/preserveRotation" value="true"/>
            <property key="labeling/previewBkgrdColor" value="#ffffff"/>
            <property key="labeling/priority" value="10"/>
            <property key="labeling/quadOffset" value="4"/>
            <property key="labeling/repeatDistance" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMaxScale" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMinScale" value="0"/>
            <property key="labeling/repeatDistanceUnit" value="1"/>
            <property key="labeling/reverseDirectionSymbol" value="false"/>
            <property key="labeling/rightDirectionSymbol" value=">"/>
            <property key="labeling/scaleMax" value="1000000"/>
            <property key="labeling/scaleMin" value="1"/>
            <property key="labeling/scaleVisibility" value="true"/>
            <property key="labeling/shadowBlendMode" value="6"/>
            <property key="labeling/shadowColorB" value="0"/>
            <property key="labeling/shadowColorG" value="0"/>
            <property key="labeling/shadowColorR" value="0"/>
            <property key="labeling/shadowDraw" value="true"/>
            <property key="labeling/shadowOffsetAngle" value="135"/>
            <property key="labeling/shadowOffsetDist" value="1"/>
            <property key="labeling/shadowOffsetGlobal" value="true"/>
            <property key="labeling/shadowOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shadowOffsetUnits" value="1"/>
            <property key="labeling/shadowRadius" value="1.5"/>
            <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
            <property key="labeling/shadowRadiusMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowRadiusMapUnitMinScale" value="0"/>
            <property key="labeling/shadowRadiusUnits" value="1"/>
            <property key="labeling/shadowScale" value="100"/>
            <property key="labeling/shadowTransparency" value="30"/>
            <property key="labeling/shadowUnder" value="0"/>
            <property key="labeling/shapeBlendMode" value="0"/>
            <property key="labeling/shapeBorderColorA" value="255"/>
            <property key="labeling/shapeBorderColorB" value="128"/>
            <property key="labeling/shapeBorderColorG" value="128"/>
            <property key="labeling/shapeBorderColorR" value="128"/>
            <property key="labeling/shapeBorderWidth" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMinScale" value="0"/>
            <property key="labeling/shapeBorderWidthUnits" value="1"/>
            <property key="labeling/shapeDraw" value="true"/>
            <property key="labeling/shapeFillColorA" value="255"/>
            <property key="labeling/shapeFillColorB" value="255"/>
            <property key="labeling/shapeFillColorG" value="255"/>
            <property key="labeling/shapeFillColorR" value="255"/>
            <property key="labeling/shapeJoinStyle" value="64"/>
            <property key="labeling/shapeOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shapeOffsetUnits" value="1"/>
            <property key="labeling/shapeOffsetX" value="0"/>
            <property key="labeling/shapeOffsetY" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMinScale" value="0"/>
            <property key="labeling/shapeRadiiUnits" value="1"/>
            <property key="labeling/shapeRadiiX" value="0"/>
            <property key="labeling/shapeRadiiY" value="0"/>
            <property key="labeling/shapeRotation" value="0"/>
            <property key="labeling/shapeRotationType" value="0"/>
            <property key="labeling/shapeSVGFile" value=""/>
            <property key="labeling/shapeSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeSizeMapUnitMinScale" value="0"/>
            <property key="labeling/shapeSizeType" value="0"/>
            <property key="labeling/shapeSizeUnits" value="1"/>
            <property key="labeling/shapeSizeX" value="0"/>
            <property key="labeling/shapeSizeY" value="0"/>
            <property key="labeling/shapeTransparency" value="0"/>
            <property key="labeling/shapeType" value="0"/>
            <property key="labeling/textColorA" value="255"/>
            <property key="labeling/textColorB" value="0"/>
            <property key="labeling/textColorG" value="0"/>
            <property key="labeling/textColorR" value="0"/>
            <property key="labeling/textTransp" value="13"/>
            <property key="labeling/upsidedownLabels" value="0"/>
            <property key="labeling/wrapChar" value=""/>
            <property key="labeling/xOffset" value="0"/>
            <property key="labeling/yOffset" value="0"/>
          </customproperties>
          <blendMode>0</blendMode>
          <featureBlendMode>0</featureBlendMode>
          <layerTransparency>55</layerTransparency>
          <displayfield>id</displayfield>
          <label>0</label>
          <labelattributes>
            <label fieldname="" text="Beschriftung"/>
            <family fieldname="" name="MS Shell Dlg 2"/>
            <size fieldname="" units="pt" value="12"/>
            <bold fieldname="" on="0"/>
            <italic fieldname="" on="0"/>
            <underline fieldname="" on="0"/>
            <strikeout fieldname="" on="0"/>
            <color fieldname="" red="0" blue="0" green="0"/>
            <x fieldname=""/>
            <y fieldname=""/>
            <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
            <angle fieldname="" value="0" auto="0"/>
            <alignment fieldname="" value="center"/>
            <buffercolor fieldname="" red="255" blue="255" green="255"/>
            <buffersize fieldname="" units="pt" value="1"/>
            <bufferenabled fieldname="" on=""/>
            <multilineenabled fieldname="" on=""/>
            <selectedonly on=""/>
          </labelattributes>
          <SingleCategoryDiagramRenderer diagramType="Pie">
            <DiagramCategory penColor="#000000" labelPlacementMethod="XHeight" penWidth="0" diagramOrientation="Up" minimumSize="0" barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" backgroundColor="#ffffff" transparency="0" width="15" scaleDependency="Area" backgroundAlpha="255" angleOffset="1440" scaleBasedVisibility="0" enabled="0" height="15" sizeType="MM" minScaleDenominator="0">
              <fontProperties description="Lucida Grande,13,-1,5,50,0,0,0,0,0" style=""/>
              <attribute field="" color="#000000" label=""/>
            </DiagramCategory>
          </SingleCategoryDiagramRenderer>
          <DiagramLayerSettings yPosColumn="-1" linePlacementFlags="10" placement="2" dist="0" xPosColumn="-1" priority="0" obstacle="0" showAll="1"/>
          <editform>C:/powerdata/qgis_projects/GermanyPower</editform>
          <editforminit/>
          <featformsuppress>0</featformsuppress>
          <annotationform>C:/powerdata/qgis_projects/GermanyPower</annotationform>
          <editorlayout>generatedlayout</editorlayout>
          <excludeAttributesWMS/>
          <excludeAttributesWFS/>
          <attributeactions/>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="id">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="version">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="user_id">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="tstamp">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="changeset_id">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="UniqueValues" name="power">
              <widgetv2config fieldEditable="1" labelOnTop="0" Editable="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="cables">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="wires">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="circuits">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="frequency">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="name">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
        </maplayer>
        <maplayer minimumScale="-4.65661e-10" maximumScale="1e+08" simplifyDrawingHints="1" minLabelScale="0" maxLabelScale="1e+08" simplifyDrawingTol="1" geometry="Line" simplifyMaxScale="1" type="vector" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" scaleBasedLabelVisibilityFlag="0">
          <id>vw_change_log20151204114804760</id>
          <datasource>dbname='"""+database+"""' host="""+host+""" port="""+port+""" user='"""+user+"""' password='"""+password+"""' sslmode=disable key='id' srid=4326 type=MultiLineString table="public"."vw_change_log" (way) sql=</datasource>
          <title></title>
          <abstract></abstract>
          <keywordList>
            <value></value>
          </keywordList>
          <layername>vw_change_log</layername>
          <srs>
            <spatialrefsys>
              <proj4>+proj=longlat +datum=WGS84 +no_defs</proj4>
              <srsid>3452</srsid>
              <srid>4326</srid>
              <authid>EPSG:4326</authid>
              <description>WGS 84</description>
              <projectionacronym>longlat</projectionacronym>
              <ellipsoidacronym>WGS84</ellipsoidacronym>
              <geographicflag>true</geographicflag>
            </spatialrefsys>
          </srs>
          <provider encoding="UTF-8">postgres</provider>
          <previewExpression>COALESCE( "id", '&lt;NULL>' )</previewExpression>
          <vectorjoins/>
          <expressionfields/>
          <map-layer-style-manager current="">
            <map-layer-style name=""/>
          </map-layer-style-manager>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="id">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="osm_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="tstamp">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="table_ident">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="action">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="members">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="power">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="cables">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="wires">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="circuits">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="frequency">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="hinweis">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
          <renderer-v2 symbollevels="0" type="RuleRenderer">
            <rules key="{dc76d4cb-b494-4520-b47b-ee6d7ca9b438}">
              <rule filter=" &quot;action&quot;  =  'updt' AND table_ident = 'way'" key="{387f82a1-7232-48ca-bb0b-d7038db8f2b4}" symbol="0" label="Update way"/>
              <rule filter=" &quot;action&quot;  =  'isrt'  AND table_ident = 'way'" key="{a69b6ea3-c14b-489e-ad92-d39a6b19be14}" symbol="1" label="Insert way"/>
              <rule filter=" &quot;action&quot;  =  'dlt' AND table_ident = 'way'" key="{65ee97d2-aa51-409b-947c-2f443b275c54}" symbol="2" label="Delete way"/>
              <rule filter=" &quot;action&quot;  =  'updt'  AND table_ident = 'rel'" key="{e9efd092-d540-4f47-842a-fcd02afbc75b}" symbol="3" label="Update relation"/>
              <rule filter=" &quot;action&quot;  =  'dlt'  AND table_ident = 'rel'" key="{b66240f8-61c7-4bff-abd7-a8cf93d53900}" symbol="4" label="Delete relation"/>
              <rule filter=" &quot;action&quot; ='isrt' AND &quot;table_ident&quot; ='rel'" key="{9dd426ba-b916-426d-854e-cb3bcac06aaa}" symbol="5" label="Insert Relation"/>
            </rules>
            <symbols>
              <symbol alpha="0.686275" clip_to_extent="1" type="line" name="0">
                <layer pass="1" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="53,129,180,255"/>
                  <prop k="line_style" v="dot"/>
                  <prop k="line_width" v="3.26"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="0.686275" clip_to_extent="1" type="line" name="1">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="53,129,180,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="3.26"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="2">
                <layer pass="2" class="MarkerLine" locked="0">
                  <prop k="interval" v="3"/>
                  <prop k="interval_map_unit_scale" v="0,0"/>
                  <prop k="interval_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_along_line" v="0"/>
                  <prop k="offset_along_line_map_unit_scale" v="0,0"/>
                  <prop k="offset_along_line_unit" v="MM"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="placement" v="interval"/>
                  <prop k="rotate" v="1"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                  <symbol alpha="1" clip_to_extent="1" type="marker" name="@2@0">
                    <layer pass="0" class="SimpleMarker" locked="0">
                      <prop k="angle" v="0"/>
                      <prop k="color" v="157,157,157,255"/>
                      <prop k="horizontal_anchor_point" v="1"/>
                      <prop k="name" v="line"/>
                      <prop k="offset" v="0,0"/>
                      <prop k="offset_map_unit_scale" v="0,0"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="outline_color" v="157,157,157,255"/>
                      <prop k="outline_style" v="solid"/>
                      <prop k="outline_width" v="0.8"/>
                      <prop k="outline_width_map_unit_scale" v="0,0"/>
                      <prop k="outline_width_unit" v="MM"/>
                      <prop k="scale_method" v="area"/>
                      <prop k="size" v="3.5"/>
                      <prop k="size_map_unit_scale" v="0,0"/>
                      <prop k="size_unit" v="MM"/>
                      <prop k="vertical_anchor_point" v="1"/>
                      <effect enabled="0" type="effectStack">
                        <effect type="dropShadow">
                          <prop k="blend_mode" v="13"/>
                          <prop k="blur_level" v="10"/>
                          <prop k="color" v="0,0,0,255"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="offset_angle" v="135"/>
                          <prop k="offset_distance" v="2"/>
                          <prop k="offset_unit" v="MM"/>
                          <prop k="offset_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0"/>
                        </effect>
                        <effect type="outerGlow">
                          <prop k="blend_mode" v="0"/>
                          <prop k="blur_level" v="3"/>
                          <prop k="color1" v="0,0,255,255"/>
                          <prop k="color2" v="0,255,0,255"/>
                          <prop k="color_type" v="0"/>
                          <prop k="discrete" v="0"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="single_color" v="255,255,255,255"/>
                          <prop k="spread" v="2"/>
                          <prop k="spread_unit" v="MM"/>
                          <prop k="spread_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0.5"/>
                        </effect>
                        <effect type="drawSource">
                          <prop k="blend_mode" v="0"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="1"/>
                          <prop k="transparency" v="0"/>
                        </effect>
                        <effect type="innerShadow">
                          <prop k="blend_mode" v="13"/>
                          <prop k="blur_level" v="10"/>
                          <prop k="color" v="0,0,0,255"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="offset_angle" v="135"/>
                          <prop k="offset_distance" v="2"/>
                          <prop k="offset_unit" v="MM"/>
                          <prop k="offset_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0"/>
                        </effect>
                        <effect type="innerGlow">
                          <prop k="blend_mode" v="0"/>
                          <prop k="blur_level" v="3"/>
                          <prop k="color1" v="0,0,255,255"/>
                          <prop k="color2" v="0,255,0,255"/>
                          <prop k="color_type" v="0"/>
                          <prop k="discrete" v="0"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="single_color" v="255,255,255,255"/>
                          <prop k="spread" v="2"/>
                          <prop k="spread_unit" v="MM"/>
                          <prop k="spread_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0.5"/>
                        </effect>
                      </effect>
                    </layer>
                  </symbol>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="3">
                <layer pass="0" class="MarkerLine" locked="0">
                  <prop k="interval" v="3"/>
                  <prop k="interval_map_unit_scale" v="0,0"/>
                  <prop k="interval_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_along_line" v="0"/>
                  <prop k="offset_along_line_map_unit_scale" v="0,0"/>
                  <prop k="offset_along_line_unit" v="MM"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="placement" v="interval"/>
                  <prop k="rotate" v="1"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                  <symbol alpha="1" clip_to_extent="1" type="marker" name="@3@0">
                    <layer pass="0" class="SimpleMarker" locked="0">
                      <prop k="angle" v="0"/>
                      <prop k="color" v="247,243,6,255"/>
                      <prop k="horizontal_anchor_point" v="1"/>
                      <prop k="name" v="circle"/>
                      <prop k="offset" v="0,0"/>
                      <prop k="offset_map_unit_scale" v="0,0"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="outline_color" v="0,0,0,255"/>
                      <prop k="outline_style" v="solid"/>
                      <prop k="outline_width" v="0"/>
                      <prop k="outline_width_map_unit_scale" v="0,0"/>
                      <prop k="outline_width_unit" v="MM"/>
                      <prop k="scale_method" v="area"/>
                      <prop k="size" v="2"/>
                      <prop k="size_map_unit_scale" v="0,0"/>
                      <prop k="size_unit" v="MM"/>
                      <prop k="vertical_anchor_point" v="1"/>
                      <effect enabled="0" type="effectStack">
                        <effect type="dropShadow">
                          <prop k="blend_mode" v="13"/>
                          <prop k="blur_level" v="10"/>
                          <prop k="color" v="0,0,0,255"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="offset_angle" v="135"/>
                          <prop k="offset_distance" v="2"/>
                          <prop k="offset_unit" v="MM"/>
                          <prop k="offset_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0"/>
                        </effect>
                        <effect type="outerGlow">
                          <prop k="blend_mode" v="0"/>
                          <prop k="blur_level" v="3"/>
                          <prop k="color1" v="0,0,255,255"/>
                          <prop k="color2" v="0,255,0,255"/>
                          <prop k="color_type" v="0"/>
                          <prop k="discrete" v="0"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="single_color" v="255,255,255,255"/>
                          <prop k="spread" v="2"/>
                          <prop k="spread_unit" v="MM"/>
                          <prop k="spread_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0.5"/>
                        </effect>
                        <effect type="drawSource">
                          <prop k="blend_mode" v="0"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="1"/>
                          <prop k="transparency" v="0"/>
                        </effect>
                        <effect type="innerShadow">
                          <prop k="blend_mode" v="13"/>
                          <prop k="blur_level" v="10"/>
                          <prop k="color" v="0,0,0,255"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="offset_angle" v="135"/>
                          <prop k="offset_distance" v="2"/>
                          <prop k="offset_unit" v="MM"/>
                          <prop k="offset_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0"/>
                        </effect>
                        <effect type="innerGlow">
                          <prop k="blend_mode" v="0"/>
                          <prop k="blur_level" v="3"/>
                          <prop k="color1" v="0,0,255,255"/>
                          <prop k="color2" v="0,255,0,255"/>
                          <prop k="color_type" v="0"/>
                          <prop k="discrete" v="0"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="single_color" v="255,255,255,255"/>
                          <prop k="spread" v="2"/>
                          <prop k="spread_unit" v="MM"/>
                          <prop k="spread_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0.5"/>
                        </effect>
                      </effect>
                    </layer>
                  </symbol>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="4">
                <layer pass="2" class="MarkerLine" locked="0">
                  <prop k="interval" v="3"/>
                  <prop k="interval_map_unit_scale" v="0,0"/>
                  <prop k="interval_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_along_line" v="0"/>
                  <prop k="offset_along_line_map_unit_scale" v="0,0"/>
                  <prop k="offset_along_line_unit" v="MM"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="placement" v="interval"/>
                  <prop k="rotate" v="1"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                  <symbol alpha="1" clip_to_extent="1" type="marker" name="@4@0">
                    <layer pass="0" class="SimpleMarker" locked="0">
                      <prop k="angle" v="0"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="horizontal_anchor_point" v="1"/>
                      <prop k="name" v="line"/>
                      <prop k="offset" v="0,0"/>
                      <prop k="offset_map_unit_scale" v="0,0"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="outline_color" v="0,0,0,255"/>
                      <prop k="outline_style" v="solid"/>
                      <prop k="outline_width" v="0.4"/>
                      <prop k="outline_width_map_unit_scale" v="0,0"/>
                      <prop k="outline_width_unit" v="MM"/>
                      <prop k="scale_method" v="area"/>
                      <prop k="size" v="3.5"/>
                      <prop k="size_map_unit_scale" v="0,0"/>
                      <prop k="size_unit" v="MM"/>
                      <prop k="vertical_anchor_point" v="1"/>
                      <effect enabled="0" type="effectStack">
                        <effect type="dropShadow">
                          <prop k="blend_mode" v="13"/>
                          <prop k="blur_level" v="10"/>
                          <prop k="color" v="0,0,0,255"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="offset_angle" v="135"/>
                          <prop k="offset_distance" v="2"/>
                          <prop k="offset_unit" v="MM"/>
                          <prop k="offset_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0"/>
                        </effect>
                        <effect type="outerGlow">
                          <prop k="blend_mode" v="0"/>
                          <prop k="blur_level" v="3"/>
                          <prop k="color1" v="0,0,255,255"/>
                          <prop k="color2" v="0,255,0,255"/>
                          <prop k="color_type" v="0"/>
                          <prop k="discrete" v="0"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="single_color" v="255,255,255,255"/>
                          <prop k="spread" v="2"/>
                          <prop k="spread_unit" v="MM"/>
                          <prop k="spread_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0.5"/>
                        </effect>
                        <effect type="drawSource">
                          <prop k="blend_mode" v="0"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="1"/>
                          <prop k="transparency" v="0"/>
                        </effect>
                        <effect type="innerShadow">
                          <prop k="blend_mode" v="13"/>
                          <prop k="blur_level" v="10"/>
                          <prop k="color" v="0,0,0,255"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="offset_angle" v="135"/>
                          <prop k="offset_distance" v="2"/>
                          <prop k="offset_unit" v="MM"/>
                          <prop k="offset_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0"/>
                        </effect>
                        <effect type="innerGlow">
                          <prop k="blend_mode" v="0"/>
                          <prop k="blur_level" v="3"/>
                          <prop k="color1" v="0,0,255,255"/>
                          <prop k="color2" v="0,255,0,255"/>
                          <prop k="color_type" v="0"/>
                          <prop k="discrete" v="0"/>
                          <prop k="draw_mode" v="2"/>
                          <prop k="enabled" v="0"/>
                          <prop k="single_color" v="255,255,255,255"/>
                          <prop k="spread" v="2"/>
                          <prop k="spread_unit" v="MM"/>
                          <prop k="spread_unit_scale" v="0,0"/>
                          <prop k="transparency" v="0.5"/>
                        </effect>
                      </effect>
                    </layer>
                  </symbol>
                </layer>
              </symbol>
              <symbol alpha="1" clip_to_extent="1" type="line" name="5">
                <layer pass="0" class="SimpleLine" locked="0">
                  <prop k="capstyle" v="square"/>
                  <prop k="customdash" v="5;2"/>
                  <prop k="customdash_map_unit_scale" v="0,0"/>
                  <prop k="customdash_unit" v="MM"/>
                  <prop k="draw_inside_polygon" v="0"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="line_color" v="247,243,6,255"/>
                  <prop k="line_style" v="solid"/>
                  <prop k="line_width" v="2"/>
                  <prop k="line_width_unit" v="MM"/>
                  <prop k="offset" v="0"/>
                  <prop k="offset_map_unit_scale" v="0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="use_custom_dash" v="0"/>
                  <prop k="width_map_unit_scale" v="0,0"/>
                  <effect enabled="0" type="effectStack">
                    <effect type="dropShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="outerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                    <effect type="drawSource">
                      <prop k="blend_mode" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="1"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerShadow">
                      <prop k="blend_mode" v="13"/>
                      <prop k="blur_level" v="10"/>
                      <prop k="color" v="0,0,0,255"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="offset_angle" v="135"/>
                      <prop k="offset_distance" v="2"/>
                      <prop k="offset_unit" v="MM"/>
                      <prop k="offset_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0"/>
                    </effect>
                    <effect type="innerGlow">
                      <prop k="blend_mode" v="0"/>
                      <prop k="blur_level" v="3"/>
                      <prop k="color1" v="0,0,255,255"/>
                      <prop k="color2" v="0,255,0,255"/>
                      <prop k="color_type" v="0"/>
                      <prop k="discrete" v="0"/>
                      <prop k="draw_mode" v="2"/>
                      <prop k="enabled" v="0"/>
                      <prop k="single_color" v="255,255,255,255"/>
                      <prop k="spread" v="2"/>
                      <prop k="spread_unit" v="MM"/>
                      <prop k="spread_unit_scale" v="0,0"/>
                      <prop k="transparency" v="0.5"/>
                    </effect>
                  </effect>
                </layer>
              </symbol>
            </symbols>
            <effect enabled="0" type="effectStack">
              <effect type="dropShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="outerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
              <effect type="drawSource">
                <prop k="blend_mode" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="1"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerShadow">
                <prop k="blend_mode" v="13"/>
                <prop k="blur_level" v="10"/>
                <prop k="color" v="0,0,0,255"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="offset_angle" v="135"/>
                <prop k="offset_distance" v="2"/>
                <prop k="offset_unit" v="MM"/>
                <prop k="offset_unit_scale" v="0,0"/>
                <prop k="transparency" v="0"/>
              </effect>
              <effect type="innerGlow">
                <prop k="blend_mode" v="0"/>
                <prop k="blur_level" v="3"/>
                <prop k="color1" v="0,0,255,255"/>
                <prop k="color2" v="0,255,0,255"/>
                <prop k="color_type" v="0"/>
                <prop k="discrete" v="0"/>
                <prop k="draw_mode" v="2"/>
                <prop k="enabled" v="0"/>
                <prop k="single_color" v="255,255,255,255"/>
                <prop k="spread" v="2"/>
                <prop k="spread_unit" v="MM"/>
                <prop k="spread_unit_scale" v="0,0"/>
                <prop k="transparency" v="0.5"/>
              </effect>
            </effect>
          </renderer-v2>
          <customproperties>
            <property key="labeling" value="pal"/>
            <property key="labeling/addDirectionSymbol" value="false"/>
            <property key="labeling/angleOffset" value="0"/>
            <property key="labeling/blendMode" value="0"/>
            <property key="labeling/bufferBlendMode" value="0"/>
            <property key="labeling/bufferColorA" value="255"/>
            <property key="labeling/bufferColorB" value="255"/>
            <property key="labeling/bufferColorG" value="255"/>
            <property key="labeling/bufferColorR" value="255"/>
            <property key="labeling/bufferDraw" value="false"/>
            <property key="labeling/bufferJoinStyle" value="64"/>
            <property key="labeling/bufferNoFill" value="false"/>
            <property key="labeling/bufferSize" value="1"/>
            <property key="labeling/bufferSizeInMapUnits" value="false"/>
            <property key="labeling/bufferSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/bufferSizeMapUnitMinScale" value="0"/>
            <property key="labeling/bufferTransp" value="0"/>
            <property key="labeling/centroidInside" value="false"/>
            <property key="labeling/centroidWhole" value="false"/>
            <property key="labeling/decimals" value="3"/>
            <property key="labeling/displayAll" value="false"/>
            <property key="labeling/dist" value="0"/>
            <property key="labeling/distInMapUnits" value="false"/>
            <property key="labeling/distMapUnitMaxScale" value="0"/>
            <property key="labeling/distMapUnitMinScale" value="0"/>
            <property key="labeling/enabled" value="false"/>
            <property key="labeling/fieldName" value=""/>
            <property key="labeling/fontBold" value="false"/>
            <property key="labeling/fontCapitals" value="0"/>
            <property key="labeling/fontFamily" value="Lucida Grande"/>
            <property key="labeling/fontItalic" value="false"/>
            <property key="labeling/fontLetterSpacing" value="0"/>
            <property key="labeling/fontLimitPixelSize" value="false"/>
            <property key="labeling/fontMaxPixelSize" value="10000"/>
            <property key="labeling/fontMinPixelSize" value="3"/>
            <property key="labeling/fontSize" value="8.25"/>
            <property key="labeling/fontSizeInMapUnits" value="false"/>
            <property key="labeling/fontSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/fontSizeMapUnitMinScale" value="0"/>
            <property key="labeling/fontStrikeout" value="false"/>
            <property key="labeling/fontUnderline" value="false"/>
            <property key="labeling/fontWeight" value="50"/>
            <property key="labeling/fontWordSpacing" value="0"/>
            <property key="labeling/formatNumbers" value="false"/>
            <property key="labeling/isExpression" value="true"/>
            <property key="labeling/labelOffsetInMapUnits" value="true"/>
            <property key="labeling/labelOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/labelOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/labelPerPart" value="false"/>
            <property key="labeling/leftDirectionSymbol" value="&lt;"/>
            <property key="labeling/limitNumLabels" value="false"/>
            <property key="labeling/maxCurvedCharAngleIn" value="20"/>
            <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
            <property key="labeling/maxNumLabels" value="2000"/>
            <property key="labeling/mergeLines" value="false"/>
            <property key="labeling/minFeatureSize" value="0"/>
            <property key="labeling/multilineAlign" value="0"/>
            <property key="labeling/multilineHeight" value="1"/>
            <property key="labeling/namedStyle" value="Normal"/>
            <property key="labeling/obstacle" value="true"/>
            <property key="labeling/placeDirectionSymbol" value="0"/>
            <property key="labeling/placement" value="2"/>
            <property key="labeling/placementFlags" value="10"/>
            <property key="labeling/plussign" value="false"/>
            <property key="labeling/preserveRotation" value="true"/>
            <property key="labeling/previewBkgrdColor" value="#ffffff"/>
            <property key="labeling/priority" value="5"/>
            <property key="labeling/quadOffset" value="4"/>
            <property key="labeling/repeatDistance" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMaxScale" value="0"/>
            <property key="labeling/repeatDistanceMapUnitMinScale" value="0"/>
            <property key="labeling/repeatDistanceUnit" value="1"/>
            <property key="labeling/reverseDirectionSymbol" value="false"/>
            <property key="labeling/rightDirectionSymbol" value=">"/>
            <property key="labeling/scaleMax" value="10000000"/>
            <property key="labeling/scaleMin" value="1"/>
            <property key="labeling/scaleVisibility" value="false"/>
            <property key="labeling/shadowBlendMode" value="6"/>
            <property key="labeling/shadowColorB" value="0"/>
            <property key="labeling/shadowColorG" value="0"/>
            <property key="labeling/shadowColorR" value="0"/>
            <property key="labeling/shadowDraw" value="false"/>
            <property key="labeling/shadowOffsetAngle" value="135"/>
            <property key="labeling/shadowOffsetDist" value="1"/>
            <property key="labeling/shadowOffsetGlobal" value="true"/>
            <property key="labeling/shadowOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shadowOffsetUnits" value="1"/>
            <property key="labeling/shadowRadius" value="1.5"/>
            <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
            <property key="labeling/shadowRadiusMapUnitMaxScale" value="0"/>
            <property key="labeling/shadowRadiusMapUnitMinScale" value="0"/>
            <property key="labeling/shadowRadiusUnits" value="1"/>
            <property key="labeling/shadowScale" value="100"/>
            <property key="labeling/shadowTransparency" value="30"/>
            <property key="labeling/shadowUnder" value="0"/>
            <property key="labeling/shapeBlendMode" value="0"/>
            <property key="labeling/shapeBorderColorA" value="255"/>
            <property key="labeling/shapeBorderColorB" value="128"/>
            <property key="labeling/shapeBorderColorG" value="128"/>
            <property key="labeling/shapeBorderColorR" value="128"/>
            <property key="labeling/shapeBorderWidth" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeBorderWidthMapUnitMinScale" value="0"/>
            <property key="labeling/shapeBorderWidthUnits" value="1"/>
            <property key="labeling/shapeDraw" value="false"/>
            <property key="labeling/shapeFillColorA" value="255"/>
            <property key="labeling/shapeFillColorB" value="255"/>
            <property key="labeling/shapeFillColorG" value="255"/>
            <property key="labeling/shapeFillColorR" value="255"/>
            <property key="labeling/shapeJoinStyle" value="64"/>
            <property key="labeling/shapeOffsetMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeOffsetMapUnitMinScale" value="0"/>
            <property key="labeling/shapeOffsetUnits" value="1"/>
            <property key="labeling/shapeOffsetX" value="0"/>
            <property key="labeling/shapeOffsetY" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeRadiiMapUnitMinScale" value="0"/>
            <property key="labeling/shapeRadiiUnits" value="1"/>
            <property key="labeling/shapeRadiiX" value="0"/>
            <property key="labeling/shapeRadiiY" value="0"/>
            <property key="labeling/shapeRotation" value="0"/>
            <property key="labeling/shapeRotationType" value="0"/>
            <property key="labeling/shapeSVGFile" value=""/>
            <property key="labeling/shapeSizeMapUnitMaxScale" value="0"/>
            <property key="labeling/shapeSizeMapUnitMinScale" value="0"/>
            <property key="labeling/shapeSizeType" value="0"/>
            <property key="labeling/shapeSizeUnits" value="1"/>
            <property key="labeling/shapeSizeX" value="0"/>
            <property key="labeling/shapeSizeY" value="0"/>
            <property key="labeling/shapeTransparency" value="0"/>
            <property key="labeling/shapeType" value="0"/>
            <property key="labeling/textColorA" value="255"/>
            <property key="labeling/textColorB" value="0"/>
            <property key="labeling/textColorG" value="0"/>
            <property key="labeling/textColorR" value="0"/>
            <property key="labeling/textTransp" value="0"/>
            <property key="labeling/upsidedownLabels" value="0"/>
            <property key="labeling/wrapChar" value=""/>
            <property key="labeling/xOffset" value="0"/>
            <property key="labeling/yOffset" value="0"/>
          </customproperties>
          <blendMode>0</blendMode>
          <featureBlendMode>0</featureBlendMode>
          <layerTransparency>0</layerTransparency>
          <displayfield>id</displayfield>
          <label>0</label>
          <labelattributes>
            <label fieldname="" text="Beschriftung"/>
            <family fieldname="" name="MS Shell Dlg 2"/>
            <size fieldname="" units="pt" value="12"/>
            <bold fieldname="" on="0"/>
            <italic fieldname="" on="0"/>
            <underline fieldname="" on="0"/>
            <strikeout fieldname="" on="0"/>
            <color fieldname="" red="0" blue="0" green="0"/>
            <x fieldname=""/>
            <y fieldname=""/>
            <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
            <angle fieldname="" value="0" auto="0"/>
            <alignment fieldname="" value="center"/>
            <buffercolor fieldname="" red="255" blue="255" green="255"/>
            <buffersize fieldname="" units="pt" value="1"/>
            <bufferenabled fieldname="" on=""/>
            <multilineenabled fieldname="" on=""/>
            <selectedonly on=""/>
          </labelattributes>
          <SingleCategoryDiagramRenderer diagramType="Pie">
            <DiagramCategory penColor="#000000" labelPlacementMethod="XHeight" penWidth="0" diagramOrientation="Up" minimumSize="0" barWidth="5" penAlpha="255" maxScaleDenominator="1e+08" backgroundColor="#ffffff" transparency="0" width="15" scaleDependency="Area" backgroundAlpha="255" angleOffset="1440" scaleBasedVisibility="0" enabled="0" height="15" sizeType="MM" minScaleDenominator="0">
              <fontProperties description="Lucida Grande,13,-1,5,50,0,0,0,0,0" style=""/>
              <attribute field="" color="#000000" label=""/>
            </DiagramCategory>
          </SingleCategoryDiagramRenderer>
          <DiagramLayerSettings yPosColumn="-1" linePlacementFlags="10" placement="2" dist="0" xPosColumn="-1" priority="0" obstacle="0" showAll="1"/>
          <editform>.</editform>
          <editforminit/>
          <featformsuppress>0</featformsuppress>
          <annotationform>.</annotationform>
          <editorlayout>generatedlayout</editorlayout>
          <excludeAttributesWMS/>
          <excludeAttributesWFS/>
          <attributeactions/>
          <edittypes>
            <edittype widgetv2type="TextEdit" name="id">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="osm_id">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="tstamp">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="table_ident">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="action">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="members">
              <widgetv2config IsMultiline="0" fieldEditable="0" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="power">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="voltage">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="cables">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="wires">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="circuits">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="frequency">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
            <edittype widgetv2type="TextEdit" name="hinweis">
              <widgetv2config IsMultiline="0" fieldEditable="1" UseHtml="0" labelOnTop="0"/>
            </edittype>
          </edittypes>
        </maplayer>
      </projectlayers>
      <properties>
        <WMSContactPerson type="QString"></WMSContactPerson>
        <WMSOnlineResource type="QString"></WMSOnlineResource>
        <WMSUseLayerIDs type="bool">false</WMSUseLayerIDs>
        <WMSContactOrganization type="QString"></WMSContactOrganization>
        <WMSKeywordList type="QStringList">
          <value></value>
        </WMSKeywordList>
        <WFSUrl type="QString"></WFSUrl>
        <Paths>
          <Absolute type="bool">false</Absolute>
        </Paths>
        <WMSServiceTitle type="QString"></WMSServiceTitle>
        <WFSLayers type="QStringList"/>
        <WMSContactMail type="QString"></WMSContactMail>
        <PositionPrecision>
          <DecimalPlaces type="int">2</DecimalPlaces>
          <Automatic type="bool">true</Automatic>
          <DegreeFormat type="QString">D</DegreeFormat>
        </PositionPrecision>
        <WCSUrl type="QString"></WCSUrl>
        <WMSContactPhone type="QString"></WMSContactPhone>
        <WMSServiceCapabilities type="bool">false</WMSServiceCapabilities>
        <WMSServiceAbstract type="QString"></WMSServiceAbstract>
        <WMSAddWktGeometry type="bool">false</WMSAddWktGeometry>
        <Measure>
          <Ellipsoid type="QString">WGS84</Ellipsoid>
        </Measure>
        <WMSPrecision type="QString">8</WMSPrecision>
        <WFSTLayers>
          <Insert type="QStringList"/>
          <Update type="QStringList"/>
          <Delete type="QStringList"/>
        </WFSTLayers>
        <PAL>
          <SearchMethod type="int">0</SearchMethod>
          <ShowingShadowRects type="bool">false</ShowingShadowRects>
          <CandidatesPolygon type="int">8</CandidatesPolygon>
          <ShowingCandidates type="bool">false</ShowingCandidates>
          <ShowingPartialsLabels type="bool">true</ShowingPartialsLabels>
          <CandidatesLine type="int">8</CandidatesLine>
          <CandidatesPoint type="int">8</CandidatesPoint>
          <ShowingAllLabels type="bool">false</ShowingAllLabels>
          <DrawOutlineLabels type="bool">true</DrawOutlineLabels>
        </PAL>
        <Gui>
          <SelectionColorBluePart type="int">0</SelectionColorBluePart>
          <CanvasColorGreenPart type="int">255</CanvasColorGreenPart>
          <CanvasColorRedPart type="int">255</CanvasColorRedPart>
          <SelectionColorRedPart type="int">255</SelectionColorRedPart>
          <SelectionColorAlphaPart type="int">255</SelectionColorAlphaPart>
          <SelectionColorGreenPart type="int">255</SelectionColorGreenPart>
          <CanvasColorBluePart type="int">255</CanvasColorBluePart>
        </Gui>
        <Digitizing>
          <DefaultSnapToleranceUnit type="int">1</DefaultSnapToleranceUnit>
          <LayerSnappingList type="QStringList">
            <value>edit_power_relations20151214185446433</value>
            <value>power_ways20151204114804618</value>
            <value>vw_change_log20151204114804760</value>
          </LayerSnappingList>
          <LayerSnappingEnabledList type="QStringList">
            <value>disabled</value>
            <value>disabled</value>
            <value>disabled</value>
          </LayerSnappingEnabledList>
          <SnappingMode type="QString">current_layer</SnappingMode>
          <AvoidIntersectionsList type="QStringList"/>
          <LayerSnappingToleranceUnitList type="QStringList">
            <value>2</value>
            <value>2</value>
            <value>2</value>
          </LayerSnappingToleranceUnitList>
          <LayerSnapToList type="QStringList">
            <value>to_vertex_and_segment</value>
            <value>to_vertex_and_segment</value>
            <value>to_vertex_and_segment</value>
          </LayerSnapToList>
          <DefaultSnapType type="QString">to vertex</DefaultSnapType>
          <DefaultSnapTolerance type="double">15</DefaultSnapTolerance>
          <TopologicalEditing type="bool">true</TopologicalEditing>
          <LayerSnappingToleranceList type="QStringList">
            <value>0.000000</value>
            <value>0.000000</value>
            <value>0.000000</value>
          </LayerSnappingToleranceList>
        </Digitizing>
        <Identify>
          <disabledLayers type="QStringList"/>
        </Identify>
        <Macros>
          <pythonCode type="QString"></pythonCode>
        </Macros>
        <WMSAccessConstraints type="QString"></WMSAccessConstraints>
        <WCSLayers type="QStringList"/>
        <Legend>
          <filterByMap type="bool">false</filterByMap>
        </Legend>
        <SpatialRefSys>
          <ProjectCRSProj4String type="QString">+proj=longlat +datum=WGS84 +no_defs</ProjectCRSProj4String>
          <ProjectCrs type="QString">EPSG:4326</ProjectCrs>
          <ProjectCRSID type="int">3452</ProjectCRSID>
          <ProjectionsEnabled type="int">1</ProjectionsEnabled>
        </SpatialRefSys>
        <DefaultStyles>
          <Fill type="QString"></Fill>
          <Line type="QString"></Line>
          <Marker type="QString"></Marker>
          <RandomColors type="bool">true</RandomColors>
          <AlphaInt type="int">255</AlphaInt>
          <ColorRamp type="QString"></ColorRamp>
        </DefaultStyles>
        <WMSFees type="QString"></WMSFees>
        <WMSImageQuality type="int">90</WMSImageQuality>
        <WMSUrl type="QString"></WMSUrl>
      </properties>
    </qgis>

    """

    filepath = qgis_proj_dir + "/" + database + "_grid_devel_project.qgs"

    if os.path.exists(filepath) == False:
        fh = open(filepath ,"w")
        fh.write(grid_devel_project)
        fh.close()