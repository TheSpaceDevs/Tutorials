FULL CHANGELOG

NEW MODELS
• added the CelestialBody model (+ CelestialBodyType config), used as FK in the Location, LandingLocation, and Orbit
models.
• added the Country config to replace string-based information in the Agency, Astronaut, Location, and Pad models
• added the Image and ImageVariant models (+ ImageLicense and ImageVariantType configs), used as FK in place of almost
all previous image_url, profile_url, logo_url, etc. fields across many models
• added the LauncherConfigurationFamily model, used as FK in the LauncherConfiguration model
• added the Payload and PayloadFlight models (+ PayloadType config)
• added the SocialMediaLink model (+ SocialMedia config), used as M2M in the Astronaut and Agency models
• added the SpacecraftConfigurationFamily model, used as M2M in the SpacecraftConfiguration model
• added the SpacecraftConfigurationType config, used as FK in the SpacecraftConfiguration model

NEW FIELDS ON EXISTING MODELS
• added the active and image fields to Location and Pad models
• added the duration and turn_around_time duration fields to the SpacecraftFlight model
• added the fastest_turnaround duration fields to the Pad, Launcher, LauncherConfiguration,
Spacecraft, and SpacecraftConfiguration models
• added the is_placeholder field to the Launcher model
• added the is_placeholder field to the LauncherConfig model (for cases where the exact
variant is not known yet, e.g. a generic Vulcan Centaur or Ariane 6)
• added the live boolean field to the VidURL model, and automated it
• added payload and spacecraft landing statistics to the Agency model
• added stats to the SpacecraftConfiguration model

FIELD/FILTER RENAMING & REORGANIZATION
• moved the launch_designator field (unpopulated so far) from the Mission model to the Launch model, and automated it
• renamed the docked field in the SpaceStation model to currently_docked
• renamed the infoURLs and vidURLs fields in the Launch model to info_urls and vid_urls
• renamed the location field in the Landing model to landing_location
• renamed the manufacturer filter on the SpacecraftConfiguration endpoint to agency, to match the filtering field
• renamed the nation_url field in the Agency model to social_icon

TYPE & FORMAT CHANGES
• made the founding_year field an integer in the Agency model
• made the latitude and longitude fields floats in the Location and Pad models
• made the spacecraft_stage field in the Rocket model an M2M relation to the SpacecraftFlight model
• made the status, net, window_start and window_end fields non-nullable in the Launch model
• made the status field in the Launcher model a LauncherStatus FK, and added filtering by FK ID on the endpoint
• made the type field in the Agency model a FK to the AgencyType config
• replaced the agency_id field in the Pad model with an M2M relation to the Agency model
• replaced the turn_around_time_days integer field in the FirstStage model by a turn_around_time duration field
• reworked the DockingEvent model to use a chaser and a target, which can be a Spacecraft, SpaceStation, or Payload FK
• reworked the DockingLocation model to make it have both a Spacecraft FK and a Payload FK

FIELD REMOVALS
• removed the holdreason field from the Launch model
• removed the launch_library_url fields from all models where it was still present (remains from the LL1 era)
• removed the news_url and video_url fields from the Event model (replaced by InfoURL and VidURL M2Ms like for launches)
• removed the r_spacex_api_id field from the Launch model and the associated filter on the endpoint (API deprecated)
• removed the the nation_url field from the SpacecraftConfiguration model
• removed the twitter and instagram fields from the Astronaut model
• removed the vehicle_range field from the LauncherConfiguration model

MISC
• added the Payload Deployed (ID 9) launch status, returned as In Flight (ID 6) in older versions

API & ENDPOINT ENHANCEMENTS
• added admin panel validations to prevent common human errors (e.g. multiple librarians saving simultaneously)
• automated the endpoint docs to provide fully exhaustive filtering, sorting, ordering, and generic information
• major refactor of all serializers to clean up code and allow full tests coverage, this means
some fields might have been added/removed to/from the list and normal modes
• major refactor all endpoints to ensure polymorphism is properly documented in the schema
• removed the non-strict LSP & location filtering option from the Launch endpoint that prevented filter documentation
• renamed all endpoint URLs to use plural and snake_case
• significant database-related performance improvements on all endpoints