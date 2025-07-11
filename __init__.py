# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QgisOpenLayersMap
                                 A QGIS plugin
 This plugins generates an OpenLayers-based web page from your QGIS project
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-07-10
        copyright            : (C) 2025 by Wiktor Lataowicz
        email                : qgis@wiktor.latanowicz.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QgisOpenLayersMap class from file QgisOpenLayersMap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qgis_open_layers_map import QgisOpenLayersMap
    return QgisOpenLayersMap(iface)
