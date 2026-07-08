---
title: "Optical Tactile Sensing"
type: concept
tags: [robotics, sensors, tactile-sensing, hardware]
sources: [cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53]
last_updated: 2026-07-08
---

# Optical Tactile Sensing

Optical tactile sensing is the source's preferred name for the visual-tactile route in robot touch. In [[cong-hui-tiaowu-dao-you-ganzhi-chujue-shi-jiqiren-tongwang-zhineng-de-menpiao-ma-s10e19-f448a656-3004-430b-a853-79d1e77dcb53]], [[EricLiZhiqiang]] says the route is still tactile rather than ordinary vision: it uses contact-driven skin deformation and light changes to infer force distribution, texture, friction, slip, and contact state.

The episode contrasts optical tactile sensing with older electromagnetic, piezoresistive, and capacitive routes. [[YimuTechnology]] claims that the optical route can reach far higher point density than traditional tactile sensors and can approach or exceed human touch on force sensitivity, texture, friction, normal force, and spatial density. The same source also notes remaining gaps, including temperature sensing and response-speed limitations.

## Key Claims
- Optical tactile sensing turns deformation of a soft surface into a measurable optical signal, then converts that signal into tactile quantities useful for robot control.
- The route is positioned as complementary to vision: cameras may see the object, while touch resolves contact, grip, sliding, and force.
- High sensing density matters because human fingertips have many tactile points and receptor types; sparse sensors cannot reproduce human-like dexterity.
- Materials are part of the sensing system: the soft layer must deform enough to capture texture but survive pressure, wear, and repeated rebound.
- [[YimuTechnology]] presents chips, optics, materials, algorithms, simulation, and data as one stack rather than separable components.

## Connections
- [[TactileSensing]] — broader robot-touch problem this route addresses.
- [[YimuTechnology]] and [[EricLiZhiqiang]] — company and guest explaining the route.
- [[DexterousManipulation]] — application area where force, texture, and slip feedback matter.
- [[TactileTransformerEncoder]] — model interface that could consume optical tactile signals.
