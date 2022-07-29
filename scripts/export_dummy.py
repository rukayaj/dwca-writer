from dwcawriter import Archive, Table
import os
import pandas as pd


data_core = {
    "id": [1, 2, 3],
    "scientificName": ["Abra alba", "Lanice conchilega", "Nereis diversicolor"],
    "notes": ["white", "brown", "green"],
    "year": [2008, 2009, 2010]
}
df_core = pd.DataFrame(data=data_core)

data_extension = {
    "id": [1, 2, 3],
    "measurementType": ["temperature", "temperature", "temperature"],
    "measurementValue": [12, 13, 14]
}
df_extension = pd.DataFrame(data=data_extension)

archive = Archive()
core_table = Table(spec="https://rs.gbif.org/core/dwc_occurrence_2022-02-02.xml", data=df_core, id_index=0)
archive.core = core_table
extension_table = Table(spec="https://rs.gbif.org/extension/dwc/measurements_or_facts_2022-02-02.xml", data=df_extension, id_index=0)
archive.extensions.append(extension_table)
archive.eml_text = ""

archive.export(os.path.expanduser(f"~/Desktop/temp/dummy.zip"), only_mapped_columns=True)
