### 
SELECT dref.coord_ra as ra,
       dref.coord_dec as dec,
       dref.ext_shapeHSM_HsmShapeRegauss_e1,
       dref.ext_shapeHSM_HsmShapeRegauss_e2,
       dref.objectId as id,
       dfrc.i_modelfit_CModel_instFlux
FROM dp01_dc2_catalogs.reference as dref,
     dp01_dc2_catalogs.position as dpos,
     dp01_dc2_catalogs.forced_photometry as dfrc
WHERE scisql_s2PtInBox(coord_ra, coord_dec, 20, -70, 95, 0) = 1
  AND dref.objectId = dpos.objectId
  AND dfrc.objectId = dpos.objectId
  AND dpos.detect_isPrimary = 1
  AND dfrc.i_modelfit_CModel_flag = 0
  AND dfrc.i_modelfit_CModel_instFlux > 0
  AND dref.base_SdssCentroid_flag = 0
  AND dref.base_Blendedness_abs < POWER(10, -0.375)
  AND dref.base_Blendedness_abs_instFlux IS NULL
  AND dref.base_ClassificationExtendedness_flag = 0
  AND dref. base_ClassificationExtendedness_value > 0
  AND ext_shapeHSM_HsmShapeRegauss_flag = 0
  AND dfrc.i_modelfit_CModel_flag = 0
  AND dfrc.i_modelfit_CModel_instFlux > 0
  AND dfrc.i_modelfit_CModel_instFlux/dfrc.i_modelfit_CModel_instFluxErr > 1000
  AND dref.ext_shapeHSM_HsmShapeRegauss_resolution >= 0.3
  AND dref.ext_shapeHSM_HsmShapeRegauss_sigma <= 0.4
  AND SQRT(POWER(dref.ext_shapeHSM_HsmShapeRegauss_e1, 2)+POWER(dref.ext_shapeHSM_HsmShapeRegauss_e2, 2)) < 2
  AND dref.base_PixelFlags_flag_edge = 0
  AND dref.base_PixelFlags_flag_interpolatedCenter = 0
  AND dref.base_PixelFlags_flag_saturatedCenter = 0
  AND dref.base_PixelFlags_flag_crCenter = 0
  AND dref.base_PixelFlags_flag_bad = 0
  AND dref.base_PixelFlags_flag_suspectCenter = 0
  AND dref.base_PixelFlags_flag_clipped = 0
  AND dref.deblend_skipped = 0 LIMIT 10
  
  