#
# IOT 2018LTS kernel
#  This kernel is an "enterprise style" kernel with a significant list of
#  backported features
#
# This package has a main package "standard" and a subpackage "sos"
#
# The "standard"  kernel  (the main package) is meant for running on
#  bare metal systems as well as running as a "normal" guest in
#  various hypervisors. This
#
# The "sos" kernel is specifically meant to run as DOM0 in an
#  ACRN hypervisor setup.
#

Name:           linux-iot-lts2018
Version:        4.19.0
Release:        10
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://git.kernel.org/torvalds/t/linux-4.19-rc8.tar.gz
Source1:        config-iot-lts2018
Source2:        config-iot-lts2018-sos
Source3:        cmdline-iot-lts2018
Source4:        cmdline-iot-lts2018-sos

# quilt.url: https://github.com/intel/linux-intel-quilt
# quilt:  mainline-tracking-v4.19-rc8-181017T004044Z
# config: mainline-tracking-v4.19-rc8-181017T004044Z

%define ktarget0 iot-lts2018
%define kversion0 %{version}-%{release}.%{ktarget0}
%define ktarget1 iot-lts2018-sos
%define kversion1 %{version}-%{release}.%{ktarget1}

BuildRequires:  buildreq-kernel

Requires: systemd-bin

# don't strip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

# PK XXXX: Series
Patch0001: 0001-greybus-Remove-android-make-file.patch
Patch0002: 0002-x86-mm-init32-Mark-text-and-rodata-RO-in-one-go.patch
Patch0003: 0003-x86-mm-cpa-Split-rename-and-clean-up-try_preserve_la.patch
Patch0004: 0004-x86-mm-cpa-Rework-static_protections.patch
Patch0005: 0005-x86-mm-cpa-Allow-range-check-for-static-protections.patch
Patch0006: 0006-x86-mm-cpa-Add-debug-mechanism.patch
Patch0007: 0007-x86-mm-cpa-Add-large-page-preservation-statistics.patch
Patch0008: 0008-x86-mm-cpa-Avoid-static-protection-checks-on-unmap.patch
Patch0009: 0009-x86-mm-cpa-Add-sanity-check-for-existing-mappings.patch
Patch0010: 0010-x86-mm-cpa-Optimize-same-protection-check.patch
Patch0011: 0011-x86-mm-cpa-Do-the-range-check-early.patch
Patch0012: 0012-x86-mm-cpa-Avoid-the-4k-pages-check-completely.patch
Patch0013: 0013-Integration-of-CBC-line-discipline-kernel-module.patch
Patch0014: 0014-cbc-Avoid-rx-sequence-counter-mismatch-warnings.patch
Patch0015: 0015-Fix-for-cbc-kernel-driver-crash-during-warm-reboot.patch
Patch0016: 0016-mmc-core-Add-functions-for-SDIO-to-hold-re-tuning.patch
Patch0017: 0017-brcmfmac-Prevent-re-tuning-conflicting-with-wake-up.patch
Patch0018: 0018-mmc-sdhci-pci-Add-support-for-Intel-ICP.patch
Patch0019: 0019-scsi-ufshdc-pci-Add-more-Intel-PCI-Ids.patch
Patch0020: 0020-HACK-scsi-ufshc-intel-pci-Force-Data-Rate-A-for-HS-m.patch
Patch0021: 0021-HACK-mmc-sdhci-pci-Disable-DCMD-for-CNP.patch
Patch0022: 0022-scsi-ufshdc-pci-Add-yet-more-Intel-PCI-Ids.patch
Patch0023: 0023-DEBUG-ufs-query-bRefClkFreq.patch
Patch0024: 0024-DEBUG-ufs-set-bRefClkFreq-to-zero.patch
Patch0025: 0025-scsi-ufshdc-pci-Add-Intel-PCI-Ids-for-EHL.patch
Patch0026: 0026-scsi-ufshdc-pci-Add-some-more-Intel-PCI-Ids.patch
Patch0027: 0027-mmc-sdhci-pci-Add-support-for-Intel-EHL.patch
Patch0028: 0028-HACK-scsi-ufs-Add-module-parameters-max_gear-dflt_hs.patch
Patch0029: 0029-rpmb-add-Replay-Protected-Memory-Block-RPMB-subsyste.patch
Patch0030: 0030-rpmb-enable-emmc-specific-read-data-fixup.patch
Patch0031: 0031-rpmb-add-sysfs-class-ABI-documentation.patch
Patch0032: 0032-char-rpmb-add-device-attributes.patch
Patch0033: 0033-char-rpmb-provide-a-user-space-interface.patch
Patch0034: 0034-char-rpmb-add-RPMB-simulation-device.patch
Patch0035: 0035-tools-rpmb-add-RPBM-access-tool.patch
Patch0036: 0036-mmc-block-register-RPMB-partition-with-the-RPMB-subs.patch
Patch0037: 0037-scsi-ufs-revamp-string-descriptor-reading.patch
Patch0038: 0038-scsi-ufs-connect-to-RPMB-subsystem.patch
Patch0039: 0039-scsi-ufs-store-device-serial-number.patch
Patch0040: 0040-rpmb-add-nvme-rpmb-frame-type.patch
Patch0041: 0041-tools-rpmb-add-support-for-nvme-device.patch
Patch0042: 0042-nvme-connect-to-rpmb-layer.patch
Patch0043: 0043-rpmb-VRPMB-FE-create-virtio-rpmb-frontend-driver.patch
Patch0044: 0044-char-rpmb-Document-Replay-Protected-Memory-Block-RPM.patch
Patch0045: 0045-block-export-block_class-to-be-used-by-class-interfa.patch
Patch0046: 0046-mei-spd-storage-proxy-driver.patch
Patch0047: 0047-mei-spd-connect-to-the-rpmb-subsystem.patch
Patch0048: 0048-staging-Add-AVnu-based-Intel-IGB-driver.patch
Patch0049: 0049-the-igb_avb-direver-cannot-coexist-with-e1000-or-e10.patch
Patch0050: 0050-fix-some-likely-copy-paste-errors-with-some-if-block.patch
Patch0051: 0051-staging-igb_avb-Remove-non-UTF-chars-to-unbreak-scri.patch
Patch0052: 0052-staging-igb_avb-Add-PCI-dependency-to-igb_avb-Kconfi.patch
Patch0053: 0053-usb-xhci-pci-Only-create-Intel-mux-device-when-it-s-.patch
Patch0054: 0054-dwc3-setup-highspeed-to-USB3.0-on-bxtp-platform.patch
Patch0055: 0055-xhci-ext-caps.c-Add-property-to-disable-SW-switch.patch
Patch0056: 0056-roles-Enable-static-DRD-mode-for-role-switch-in-Inte.patch
Patch0057: 0057-usb-dwc3-Fix-NULL-pointer-exception-in-dwc3_pci_remo.patch
Patch0058: 0058-ACPI-battery-use-cache_time-as-cache-enabled.patch
Patch0059: 0059-alarmtimer-add-config-to-skip-suspend-flow.patch
Patch0060: 0060-Add-support-for-CNL-FPGA.patch
Patch0061: 0061-Load-nhlt-from-firmware-instead-of-debugfs.patch
Patch0062: 0062-Add-facility-to-load-ROM-via-debugfs.patch
Patch0063: 0063-ASoC-mfd-Intel-changes-for-WM8281-integration-on-K4..patch
Patch0064: 0064-ASoC-Intel-Add-CNL-Machine-Driver-with-code-wm8281.patch
Patch0065: 0065-ASoC-rt274-Force-load-rt274-without-acpi.patch
Patch0066: 0066-ASoC-HDA-EXT-Mark-dma-buffers-as-un-cacheble.patch
Patch0067: 0067-ASoC-intel-skylake-mark-ring-buffer-as-non-cacheble.patch
Patch0068: 0068-REVERTME-ASoC-Intel-CNL-Load-firmware-in-dsp_init.patch
Patch0069: 0069-ASoC-Intel-CNL-Add-library-loading-support.patch
Patch0070: 0070-Soundwire-squashed-commits.patch
Patch0071: 0071-ASoC-Add-dai_ops-to-set-the-stream-tag.patch
Patch0072: 0072-ASoC-CNL-Register-soundwire-controller-to-bus-driver.patch
Patch0073: 0073-ASoC-Intel-Add-support-for-SoundWire-link-in-copier.patch
Patch0074: 0074-ASoC-Intel-Skylake-Interface-change-between-firmware.patch
Patch0075: 0075-ASoC-Intel-Add-support-to-bypass-NHLT-reading-for-SD.patch
Patch0076: 0076-ASoC-Intel-Skylake-Add-support-for-the-SDW-dai-ops.patch
Patch0077: 0077-ASoC-CNL-Add-SoundWire-machine-file.patch
Patch0078: 0078-SoundWire-Intel-Register-4-master-controller-to-the-.patch
Patch0079: 0079-REVERTME-SDW-CNL-Register-only-3-master-controller-t.patch
Patch0080: 0080-ASoC-CNL-Add-support-for-DMIC-link-in-SDW-machine-dr.patch
Patch0081: 0081-ASoC-SKL-Add-DAI-for-the-SoundWire-PDM-interface.patch
Patch0082: 0082-Intel-ASoc-Handle-SDW-PCM-hw_params-for-PDM.patch
Patch0083: 0083-ASoC-Codecs-Add-support-for-SV-FPGA-SoundWire-PDM-Co.patch
Patch0084: 0084-ASoC-Intel-Add-machine-driver-for-SoundWire-SV-PDM-C.patch
Patch0085: 0085-SoundWire-Hardcoding-in-bus-driver-for-SVFPGA-PDM-co.patch
Patch0086: 0086-SDW-Intel-Fix-hardcoding-for-SVFPGA-codec.patch
Patch0087: 0087-REVERTME-SDW-Increment-the-dev_id-for-every-slave-re.patch
Patch0088: 0088-SDW-Support-async-messages-for-bus-driver.patch
Patch0089: 0089-SDW-Change-log-level-to-error-from-debug.patch
Patch0090: 0090-SDW-Intel-Enabled-the-Multimode-for-Intel-SDW-master.patch
Patch0091: 0091-SDW-Intel-Add-the-handler-for-async-message-transfer.patch
Patch0092: 0092-SDW-CNL-Fix-the-syncgo-functionality.patch
Patch0093: 0093-SoundWire-Remove-dead-code-from-SoundWire-BW-calcula.patch
Patch0094: 0094-REVERTME-SDW-Skip-the-Slave-programming-for-the-stre.patch
Patch0095: 0095-SoundWire-Add-support-for-the-aggregation.patch
Patch0096: 0096-REVERTME-ASoC-CNL-Mark-SDW-master-1-and-2-as-aggrega.patch
Patch0097: 0097-ASoC-CNL-Update-capabilities-fields-of-SDW-master.patch
Patch0098: 0098-ASoC-CNL-Add-support-for-aggregated-gateways.patch
Patch0099: 0099-ASoC-CNL-Add-DAIS-for-SoundWire-masters.patch
Patch0100: 0100-ASoC-core-Adds-support-for-DSP-loopback-dai-link.patch
Patch0101: 0101-ASoC-dapm-fix-stream-directions-for-dsp_loopback-lin.patch
Patch0102: 0102-ASoC-utils-add-inputs-and-outputs-to-dummy-codec.patch
Patch0103: 0103-ASoC-core-Do-not-return-for-dummy-codec-in-soc_probe.patch
Patch0104: 0104-ASoC-SKL-Fix-ch_cfg-when-fixup-is-applied.patch
Patch0105: 0105-ASoC-Intel-Skylake-Add-NHLT-override-control.patch
Patch0106: 0106-ASoC-Intel-Skylake-Add-debugfs-NHLT-ssp-override.patch
Patch0107: 0107-ASoC-Intel-Skylake-Add-debugfs-NHLT-dmic-override.patch
Patch0108: 0108-ASoC-Intel-Skylake-Read-blobs-from-debugfs-on-overri.patch
Patch0109: 0109-ASoC-Intel-Skylake-NHLT-override-check-cfg-size-in-d.patch
Patch0110: 0110-ASoC-Intel-Skylake-add-ssp-blob-override-support-for.patch
Patch0111: 0111-WORKAROUND-Remove-size-check-for-DMIC-blob.patch
Patch0112: 0112-REVERTME-SKL-Topology-Add-logic-to-create-SDW-aggreg.patch
Patch0113: 0113-SKL-PCM-Derive-the-SDW-master-controller-number-from.patch
Patch0114: 0114-REVERTME-SKL-PCM-Enable-aggregation-for-the-Maxim-co.patch
Patch0115: 0115-ASoC-Intel-Skylake-Driver-ring-buffer-APIs-for-firmw.patch
Patch0116: 0116-ASoC-Intel-Skylake-Handler-for-firmware-log-buffer-s.patch
Patch0117: 0117-ASoC-Intel-Skylake-Compress-ops-for-firmware-logging.patch
Patch0118: 0118-ASoC-Intel-Skylake-Check-buffer-users-and-prevent-co.patch
Patch0119: 0119-ASoC-Intel-Skylake-Wake-up-any-potential-reader-afte.patch
Patch0120: 0120-ASoC-Intel-Skylake-Convert-buffer-size-to-of-u32-ele.patch
Patch0121: 0121-ASoC-Intel-CNL-Initialize-trace-buffer-window-for-CN.patch
Patch0122: 0122-ASoC-Intel-Skylake-Add-trace-buffer-dais-for-CNL.patch
Patch0123: 0123-REVERTME-1-Revert-when-logging-is-updated-in-driver-.patch
Patch0124: 0124-ASoC-Intel-Skylake-Add-dsp-log-level-selection-kcont.patch
Patch0125: 0125-ASoC-Intel-CNL-Enable-SDW-aggregation-support-from-I.patch
Patch0126: 0126-ASoC-Intel-SKL-Remove-SDW-aggregation-hardcode-data.patch
Patch0127: 0127-ASoC-Intel-Aggregation-fixes-for-masters-other-than-.patch
Patch0128: 0128-ASoC-Fix-TLV-control-size-in-TLV-handler.patch
Patch0129: 0129-ALSA-hda-Enhance-HD-audio-framework-to-support-compr.patch
Patch0130: 0130-ALSA-hda-Service-buffer-completed-interrupts-for-com.patch
Patch0131: 0131-ASoC-Intel-Add-delete-module-IPC.patch
Patch0132: 0132-ASoC-Intel-Add-Probe-compress-APIs.patch
Patch0133: 0133-ASoC-Intel-Skylake-KW-fixes-for-probe-feature.patch
Patch0134: 0134-ASoC-Intel-Skylake-Probe-Start-DMA-before-setting-pr.patch
Patch0135: 0135-ASoC-Intel-Skylake-Probe-Limit-the-bytes-to-copy.patch
Patch0136: 0136-ASoC-Intel-Skylake-Probe-Increase-the-DMA-buffer-siz.patch
Patch0137: 0137-ASoC-Intel-Skylake-Probe-Increase-Injector-DMA-buffe.patch
Patch0138: 0138-ASoC-Intel-Skylake-Probe-Increase-Injector-DMA-buffe.patch
Patch0139: 0139-Soundwire-squashed-commits-2.patch
Patch0140: 0140-ALSA-core-let-low-level-driver-or-userspace-disable-.patch
Patch0141: 0141-ALSA-pcm-conditionally-avoid-mmap-of-control-data.patch
Patch0142: 0142-ALSA-hda-ext-add-spib-to-stream-context.patch
Patch0143: 0143-ASoC-Intel-Skylake-add-support-for-spib-mode.patch
Patch0144: 0144-ASoC-Intel-CNL-Fetch-ACPI-data-for-SoundWire-Master.patch
Patch0145: 0145-ASoC-Intel-CNL-get-SoundWire-Master-capabilities-and.patch
Patch0146: 0146-ASoC-Intel-CNL-Define-DPN-package-for-SDW1.patch
Patch0147: 0147-ASoC-Intel-Skylake-Support-for-24KHz-SoC-DMIC-captur.patch
Patch0148: 0148-ASoC-add-rt700-codec-driver.patch
Patch0149: 0149-ASoC-Intel-Add-support-for-ALC700-machine-driver.patch
Patch0150: 0150-ASoC-Intel-CNL-Add-new-BE-dai-for-ALC701-HS-plyaback.patch
Patch0151: 0151-ASoC-Intel-CNL-Enable-sdw-interrupt-during-D0.patch
Patch0152: 0152-ASoC-Intel-Skylake-fix-for-large-get-config-api.patch
Patch0153: 0153-ASoC-Intel-Skylake-generic-IPC-message-support.patch
Patch0154: 0154-ASoC-Intel-Skylake-Add-support-to-get-fw-configurati.patch
Patch0155: 0155-Register-masters-only-if-RT700-is-selected-in-config.patch
Patch0156: 0156-Add-if-for-platform-codec-name-in-cnl_rt700-machine.patch
Patch0157: 0157-ASoC-Intel-CNL-Change-BE-id-to-SDW-MSTR1.patch
Patch0158: 0158-ASoC-Intel-CNL-Update-dsp-ops-API-to-take-direction-.patch
Patch0159: 0159-ASoC-Intel-CNL-Platform-driver-implementation-for-So.patch
Patch0160: 0160-ASoC-Intel-CNL-Register-BRA-ops-in-init.patch
Patch0161: 0161-ASoC-rt700-codec-changes-for-BRA-feature.patch
Patch0162: 0162-ASoC-Intel-Add-support-for-Icelake-IDs.patch
Patch0163: 0163-ASoC-Intel-Fix-build-warning-for-unused-variables.patch
Patch0164: 0164-ASoC-Intel-Fix-Compilation-issues-for-probe-compress.patch
Patch0165: 0165-ASoC-Intel-Kconfig-and-Makefile-changes-for-SoundWir.patch
Patch0166: 0166-ASoC-Intel-Boards-Add-CNL-RT274-I2S-machine-driver.patch
Patch0167: 0167-ASoC-Intel-Modify-Icelake-machine-id-to-use-RT274.patch
Patch0168: 0168-ASoC-Intel-board-Add-id_table-in-cnl_rt274.patch
Patch0169: 0169-ASoC-Intel-Skylake-Support-for-all-rates-from-8K-to-.patch
Patch0170: 0170-ASoc-rt700-Fix-for-first-playback-and-capture-no-aud.patch
Patch0171: 0171-ASoC-Intel-Add-SoundWire-aggregation-support.patch
Patch0172: 0172-ASoC-Intel-Skylake-Avoid-resume-capablity-for-captur.patch
Patch0173: 0173-ASoC-Intel-Skylake-Support-all-I2S-ports-with-all-po.patch
Patch0174: 0174-ASoC-Intel-Skylake-Add-platform-DAI-for-deepbuffer-c.patch
Patch0175: 0175-ASoC-Intel-board-Enable-deepbuffer-capture-in-cnl_rt.patch
Patch0176: 0176-ASoC-Intel-Add-Icelake-machine-id-to-use-RT700.patch
Patch0177: 0177-ASoC-Intel-Add-Icelake-machine-id-to-use-WM8281.patch
Patch0178: 0178-ASoC-Intel-Skylake-Fix-library-name-length.patch
Patch0179: 0179-ASoC-Intel-Skylake-Update-SDW-BRA-interface.patch
Patch0180: 0180-ASoC-Intel-Skylake-Split-dais-and-add-flag-for-dynam.patch
Patch0181: 0181-ASoC-Intel-Skylake-Add-component-ops-for-dai-load.patch
Patch0182: 0182-ASoC-Intel-board-Add-support-for-dynamic-FE-dai-link.patch
Patch0183: 0183-ASoC-Intel-board-Add-support-for-dynamic-FE-dai-link.patch
Patch0184: 0184-ASoC-Intel-Update-device-type-entry-for-SoundWire-de.patch
Patch0185: 0185-ASoC-Intel-Skylake-Use-device-type-to-determine-Soun.patch
Patch0186: 0186-ASoC-Intel-Remove-pdi_type-support-from-topology.patch
Patch0187: 0187-ASoC-Intel-Skylake-Define-tokens-for-aggregation.patch
Patch0188: 0188-ASoC-Intel-Skylake-Parse-tokens-to-support-aggregati.patch
Patch0189: 0189-ASoC-Intel-CNL-Add-DAIs-for-SDW-Aggregation.patch
Patch0190: 0190-ASoC-Intel-Kconfig-changes-for-SoundWire-aggregation.patch
Patch0191: 0191-ASoC-rt700-codec-changes-for-SDW-Aggregation.patch
Patch0192: 0192-ASoC-Intel-Boards-Add-SDW-Aggregation-changes.patch
Patch0193: 0193-ASoC-Intel-Change-sst_ipc_tx_message_wait-api-to-ret.patch
Patch0194: 0194-ASoC-Intel-Skylake-Extract-the-receive-response-size.patch
Patch0195: 0195-ASoC-Intel-Skylake-Querying-FW-CONFIG-information.patch
Patch0196: 0196-ASoC-Intel-Skylake-Parse-the-fw-property.patch
Patch0197: 0197-ASoC-Intel-Skylake-Check-for-memory-reclaim-bit.patch
Patch0198: 0198-ASoC-Intel-Skylake-Better-handling-of-stream-interru.patch
Patch0199: 0199-ASoC-Intel-Skylake-Set-DUM-bit-in-EM2-register.patch
Patch0200: 0200-ASoC-Intel-Skylake-Add-D0i3-support-for-Icelake-plat.patch
Patch0201: 0201-ASoC-Intel-Skylake-Audio-format-mismatch-detection.patch
Patch0202: 0202-ASoC-Intel-Skylake-add-sysfs-files-for-firmware-modu.patch
Patch0203: 0203-ASoC-Intel-Skylake-Append-SDW-device-to-device-type-.patch
Patch0204: 0204-ASoC-Intel-Skylake-Debugfs-for-core-power-handling.patch
Patch0205: 0205-ASoC-Intel-Skylake-DebugFs-changes-to-suit-FDK.patch
Patch0206: 0206-ASoC-Intel-Skylake-Support-Pipeline-Properties-IPC.patch
Patch0207: 0207-ASoC-Intel-Skylake-Add-check-for-buffer-overflow.patch
Patch0208: 0208-ASoC-Intel-Skylake-Increase-the-SSP-count-in-debugFS.patch
Patch0209: 0209-ASoC-Intel-CNL-Retrieve-module-id-from-GUID.patch
Patch0210: 0210-ASoc-rt700-Remove-runtime-get-and-put-from-set-bias.patch
Patch0211: 0211-ASoC-Intel-board-Add-SSP0-codec-codec-link.patch
Patch0212: 0212-ASoC-Intel-board-Move-cnl_rt274-clock-setting-to-sup.patch
Patch0213: 0213-SoundWire-Select-default-frame-shape-based-on-platfo.patch
Patch0214: 0214-ASoC-rt700-Added-support-for-ICL-FPGA-SDW-Aggregatio.patch
Patch0215: 0215-ASoC-Intel-Boards-Add-support-for-ICL-FPGA-SDW-Aggre.patch
Patch0216: 0216-ASoC-Intel-CNL-Add-support-for-ICL-FPGA-SDW-Aggregat.patch
Patch0217: 0217-ASoC-Intel-Skylake-Add-support-for-getting-hw-config.patch
Patch0218: 0218-ASoC-Intel-Skylake-Get-dsp-core-count-from-hw-config.patch
Patch0219: 0219-ASoC-Intel-Skylake-Add-user-notification-event-for-p.patch
Patch0220: 0220-ASoC-Intel-Extract-the-nhlt-version-from-DSDT-table.patch
Patch0221: 0221-ASoC-Intel-Skylake-Increase-the-max-number-of-entrie.patch
Patch0222: 0222-ASoC-Intel-Skylake-Add-single-module-support-in-a-gi.patch
Patch0223: 0223-ASoC-Intel-Skylake-Fix-incorrect-parsing-of-pipe-tok.patch
Patch0224: 0224-ASoC-Intel-Skylake-Create-SSP-BE-dais-dynamically.patch
Patch0225: 0225-ASoC-Intel-Skylake-Adding-support-for-set-system-tim.patch
Patch0226: 0226-ASoC-Intel-Skylake-Update-FW-Trace-logs-feature-to-n.patch
Patch0227: 0227-ASoC-Intel-Skylake-Fix-FW-logging-data-corruption.patch
Patch0228: 0228-ASoC-Intel-Board-Add-BXTP-MRB-machine-driver-for-NXP.patch
Patch0229: 0229-ASoC-tdf8532-NXP-TDF8532-audio-class-D-amplifier-dri.patch
Patch0230: 0230-ASoC-Intel-Skylake-Added-support-for-creating-BXTP-G.patch
Patch0231: 0231-ASoC-Intel-boards-Remove-SSP1-codec-dai-link-from-cn.patch
Patch0232: 0232-FIX-Kconfigs-to-build-compile-with-all-platforms.patch
Patch0233: 0233-ASoC-Intel-Boards-FW-logging-DAI-links-for-BXT-P.patch
Patch0234: 0234-ASoC-Intel-Board-DAI-links-for-probe-in-APL-machine-.patch
Patch0235: 0235-ASoC-Intel-Skylake-Probe-sequence-changes-based-on-s.patch
Patch0236: 0236-ASoC-Intel-Skylake-Probe-DMA-release-for-extractor.patch
Patch0237: 0237-ASoC-Intel-Multiple-I-O-PCM-format-support-for-pipe.patch
Patch0238: 0238-ASoC-Intel-Skylake-Parse-manifest-data-to-fill-DMA-c.patch
Patch0239: 0239-ASoC-Intel-Skylake-Add-support-for-always-on-CLK-con.patch
Patch0240: 0240-ASoC-Intel-bxtn-Initialize-fw-tracing-window-for-bxt.patch
Patch0241: 0241-ASoC-Intel-Board-DAI-links-for-probe-in-GPMRB-machin.patch
Patch0242: 0242-ASoC-Intel-Boards-Add-FW-logging-DAI-links-for-GPMRB.patch
Patch0243: 0243-ASoC-Intel-Skylake-Send-correct-size-in-ipc-header-f.patch
Patch0244: 0244-ASoC-Intel-board-Add-support-for-HDMI-in-cnl_rt274.patch
Patch0245: 0245-ASoC-Intel-Skylake-Support-for-DSP-exception-record-.patch
Patch0246: 0246-ASoC-Intel-board-Separate-out-icl_rt274-from-cnl_rt2.patch
Patch0247: 0247-ASoC-Intel-Skylake-Removed-duplicate-IPC-call-for-Pr.patch
Patch0248: 0248-ASoC-Intel-Skylake-Notify-topology-changes.patch
Patch0249: 0249-ASoC-rt700-Remove-unused-variables.patch
Patch0250: 0250-ASoC-rt700-Remove-prints-used-for-debugging.patch
Patch0251: 0251-ASoC-tdf8532-Fix-compilation-warnings.patch
Patch0252: 0252-ASoC-Intel-CNL-Remove-larger-frame-size-warnings-fro.patch
Patch0253: 0253-ASoC-Intel-Skylake-Add-support-for-module-notificati.patch
Patch0254: 0254-ASoC-Intel-Board-Add-pm_ops-to-fix-suspend-resume-is.patch
Patch0255: 0255-ASoC-rt700-Remove-unused-variable.patch
Patch0256: 0256-ASoC-Intel-board-Remove-unused-function-cnl_dmic_fix.patch
Patch0257: 0257-ASoC-Intel-Skylake-Move-prototype-to-appropriate-hea.patch
Patch0258: 0258-ASoC-Intel-cnl-Move-d0i-03-ops-after-cnl_load_base_f.patch
Patch0259: 0259-ASoC-Intel-Skylake-Support-for-Probe-DMA-Buffer-size.patch
Patch0260: 0260-ASoC-Intel-Skylake-Add-a-separate-module-type-for-AS.patch
Patch0261: 0261-ASoC-Intel-Skylake-Add-support-for-DMA-Buffer-config.patch
Patch0262: 0262-ASoC-Intel-Set-all-I2S-ports-to-slave-mode-after-DSP.patch
Patch0263: 0263-ASoC-Intel-Skylake-Return-default-sampling-rate-for-.patch
Patch0264: 0264-ASoC-Intel-Board-Add-fixup-for-32-bit-masking.patch
Patch0265: 0265-ASoC-Intel-Skylake-Add-support-for-GAIN-module.patch
Patch0266: 0266-ASoC-Intel-Skylake-Fix-codec_dai-NULL-pointer-derefe.patch
Patch0267: 0267-ASoC-Intel-Skylake-Check-for-word_length_buffer-allc.patch
Patch0268: 0268-ASoC-Intel-Skylake-Fix-cnl_sdw_startup-error-path.patch
Patch0269: 0269-ASoC-Intel-Skylake-Fix-error-handling-in-cnl_sdw_hw_.patch
Patch0270: 0270-ASoC-Intel-Skylake-Check-for-NHLT-ACPI-header-signat.patch
Patch0271: 0271-ASoC-Intel-Skylake-Fix-Max-DSP-MCPS-value.patch
Patch0272: 0272-ASoC-Intel-Skylake-Fix-bug-in-module-id-retrieval-fo.patch
Patch0273: 0273-ASoC-Intel-Skylake-Fix-incorrect-in_fmt-and-out_fmt-.patch
Patch0274: 0274-ASoC-Intel-Skylake-Avoid-global-kcontrol-pointer-for.patch
Patch0275: 0275-ASoC-Intel-Skylake-Return-default-sampling-rate-for-.patch
Patch0276: 0276-ASoC-Intel-Skylake-Add-ULL-machine-driver-entry.patch
Patch0277: 0277-ASoC-Intel-Board-Add-BXTP-MRB-ULL-machine-driver.patch
Patch0278: 0278-ASoC-Intel-Skylake-Add-support-to-configure-ADSP-Sch.patch
Patch0279: 0279-WA-Disable-irq-in-rt274.patch
Patch0280: 0280-ASoC-Intel-Skylake-Replace-modulus-operator-with-div.patch
Patch0281: 0281-ASoC-Intel-Skylake-Poll-on-ADSPCS.CSTALL-bit-to-conf.patch
Patch0282: 0282-ASoC-Intel-Skylake-Add-delay-during-DSP-core-start.patch
Patch0283: 0283-ALSA-hda-Make-sure-DMA-is-stopped-by-reading-back-th.patch
Patch0284: 0284-ALSA-hda-Make-sure-DMA-is-started-by-reading-back-th.patch
Patch0285: 0285-ALSA-hda-Log-HDA-Hardware-related-errors.patch
Patch0286: 0286-ALSA-hda-check-if-stream-is-stopped-in-snd_hdac_stre.patch
Patch0287: 0287-ASoC-Intel-Skylake-Support-multiple-format-configs.patch
Patch0288: 0288-SoundWire-Fix-CRC8-dependency.patch
Patch0289: 0289-soundwire-Change-programming-sequence-for-BRA.patch
Patch0290: 0290-ASoC-tdf8532-Add-delay-while-reading-a-packet-from-I.patch
Patch0291: 0291-SoundWire-Perform-clock-exit-by-setting-clock-stop-c.patch
Patch0292: 0292-ASoC-Intel-Skylake-Add-API-to-reset-private-instance.patch
Patch0293: 0293-ASoC-Intel-Skylake-Add-an-API-to-reset-the-usage-cou.patch
Patch0294: 0294-ASoC-Intel-Skylake-Fix-the-is_dsp_running-to-return-.patch
Patch0295: 0295-ASoC-Intel-Skylake-Avoid-sending-IPCs-during-the-cra.patch
Patch0296: 0296-ASoC-Intel-CNL-Fix-for-the-firmware-redownload-failu.patch
Patch0297: 0297-ASoC-Intel-SKL-Implement-the-timer-to-trigger-firmwa.patch
Patch0298: 0298-ASoC-Intel-Skylake-Implement-recovery-for-cAVS-platf.patch
Patch0299: 0299-ASoC-Intel-Skylake-Update-gain-interface-structure.patch
Patch0300: 0300-ASoC-Intel-Skylake-Read-extended-crash-dump-info-fro.patch
Patch0301: 0301-ASoC-Intel-Skylake-Fix-issues-in-ADSP-Extended-Crash.patch
Patch0302: 0302-ASoC-Intel-kconfig-Make-drivers-build-on-x86-only.patch
Patch0303: 0303-ASoC-tdf8532-Fix-Audio-memory-leakage-at-boot-time.patch
Patch0304: 0304-ASoC-Intel-Skylake-Fix-Audio-memory-leakage-at-boot-.patch
Patch0305: 0305-ASoC-Intel-Skylake-Add-support-to-notify-resource-ev.patch
Patch0306: 0306-ASoC-Intel-BXT-Retry-FW-download-sequence.patch
Patch0307: 0307-ASoC-Intel-Skylake-Check-for-pointer-validity.patch
Patch0308: 0308-ASoC-Intel-Skylake-Fix-logs_core-array-size.patch
Patch0309: 0309-ASoC-Intel-Skylake-Replace-strcpy-with-strlcpy.patch
Patch0310: 0310-ASoC-Intel-Boards-Replace-codec-to-component-in-RT27.patch
Patch0311: 0311-ASoC-Intel-Skylake-Set-dsp-cores-off-during-shutdown.patch
Patch0312: 0312-ASoC-Intel-Disable-dsp-core-in-skl_shutdown.patch
Patch0313: 0313-ASoC-soc-pcm-Fix-FE-and-BE-race-when-accessing-subst.patch
Patch0314: 0314-Revert-ASoC-tdf8532-Fix-Audio-memory-leakage-at-boot.patch
Patch0315: 0315-ASoC-tdf8532-fix-memleak-in-tdf8532_wait_state.patch
Patch0316: 0316-ASoC-tdf8532-right-free-allocated-space-in-case-of-e.patch
Patch0317: 0317-ASoC-Intel-Skylake-Add-kabylake-R-machine-driver-ent.patch
Patch0318: 0318-ASoC-Intel-Boards-Add-machine-driver-for-Kabylake-R.patch
Patch0319: 0319-ASoC-rt298-Set-jack-combo-for-kabylake-R.patch
Patch0320: 0320-ASoC-Intel-Boards-Add-machine-driver-for-RSE-topolog.patch
Patch0321: 0321-ASoC-Intel-Boards-Add-machine-driver-for-HU-topology.patch
Patch0322: 0322-ASoC-Intel-Boards-Add-a-machine-driver-for-BXT-P-IVI.patch
Patch0323: 0323-ASoC-Intel-Boards-Add-machine-driver-for-generic-top.patch
Patch0324: 0324-ASoC-Intel-Skylake-Add-RSE-HU-M3-and-generic-machine.patch
Patch0325: 0325-ASoC-Intel-Skylake-Resolve-load-DMA-control-config-i.patch
Patch0326: 0326-ASoC-Intel-Skylake-Improve-BXT-P-machine-driver-sele.patch
Patch0327: 0327-ASoC-Intel-common-Provide-an-interface-to-send-IPCs-.patch
Patch0328: 0328-ASoC-Intel-BXT-Remove-compile-warnings.patch
Patch0329: 0329-ASoC-topology-Increase-SND_SOC_TPLG_NUM_TEXTS-to-32.patch
Patch0330: 0330-ASoC-Intel-board-Add-support-for-FE-dynamic-dai-for-.patch
Patch0331: 0331-ASoC-Intel-Skylake-Enable-use_tplg_pcm-flag-for-BXTP.patch
Patch0332: 0332-ASoC-Intel-Fix-race-condition-in-IPC-rx-list.patch
Patch0333: 0333-ASoC-Intel-Skylake-pipeline-needs-to-be-reset-before.patch
Patch0334: 0334-Revert-ASoC-topology-Increase-SND_SOC_TPLG_NUM_TEXTS.patch
Patch0335: 0335-ASoC-Intel-Allow-for-firmware-load-retry.patch
Patch0336: 0336-Revert-ASoC-core-Do-not-return-for-dummy-codec-in-so.patch
Patch0337: 0337-ASoC-Intel-Skylake-Align-with-v4.18-rc1-linux-kernel.patch
Patch0338: 0338-ASoC-Intel-Move-bxt-machine-drv-tables-to-common-dir.patch
Patch0339: 0339-ASoC-Intel-Move-kbl-machine-drv-tables-to-common-dir.patch
Patch0340: 0340-ASoC-Intel-Move-skl-machine-drv-tables-to-common-dir.patch
Patch0341: 0341-ASoC-Intel-Move-glk-machine-drv-tables-to-common-dir.patch
Patch0342: 0342-ASoC-Intel-Move-icl-machine-drv-tables-to-common-dir.patch
Patch0343: 0343-ASoC-Intel-Move-cnl-machine-drv-tables-to-common-dir.patch
Patch0344: 0344-ASoC-Intel-Skylake-validate-the-downloaded-firmware.patch
Patch0345: 0345-ASoC-Intel-Replace-hdac_ext_bus-usage-with-hdac_bus.patch
Patch0346: 0346-REVERTME-Fix-no-audio-output-after-resume-from-S3.patch
Patch0347: 0347-REVERTME-Increase-tdf8532-timeout-and-number-of-retr.patch
Patch0348: 0348-fix-the-invalid-double-free-in-tdf8532-i2c-read-erro.patch
Patch0349: 0349-ASoC-Intel-Skylake-Restore-static-SSP5-BE-declaratio.patch
Patch0350: 0350-PCI-add-pci_devices_ignore-cmdline-option.patch
Patch0351: 0351-x86-add-ACRN-hypervisor-guest.patch
Patch0352: 0352-VHM-add-vhm-char-device-driver.patch
Patch0353: 0353-VHM-add-guest-memory-management-support.patch
Patch0354: 0354-VHM-add-guest-memory-remote-mapping-support.patch
Patch0355: 0355-VHM-add-ioreq-service-support.patch
Patch0356: 0356-VHM-add-interrupt-injection-support.patch
Patch0357: 0357-VHM-add-API-to-get-vm-info.patch
Patch0358: 0358-VHM-add-API-to-do-guest-gpa2hpa-translation.patch
Patch0359: 0359-VHM-add-passthrough-device-support.patch
Patch0360: 0360-x86-acrn-add-write_msi-pv-ops-to-intercept-pci-msi-w.patch
Patch0361: 0361-sos-cleanup-hypercall-API.patch
Patch0362: 0362-vcpu-export-vcpu-create-interface-to-DM.patch
Patch0363: 0363-sos-clean-up-ptdev-msi-x-table-ioremap-operations.patch
Patch0364: 0364-sos-Update-the-common-head-file.patch
Patch0365: 0365-sos-cleanup-ptdev-irq-structure.patch
Patch0366: 0366-VBS-K-Virtio-Backend-Service-in-Kernel-a-kernel-leve.patch
Patch0367: 0367-VBS-K-virtqueue-initialization-API.patch
Patch0368: 0368-VBS-K-virtqueue-runtime-API.patch
Patch0369: 0369-VBS-K-added-a-VBS-K-reference-driver.patch
Patch0370: 0370-hypercall-refine-hypercall-interfaces.patch
Patch0371: 0371-vhm-refine-vm-related-hypercall-ioctrl.patch
Patch0372: 0372-hypercall-refine-HC-ID-and-parameter-number.patch
Patch0373: 0373-ioctl-cleanup-ioctl-structure.patch
Patch0374: 0374-Shared_buf-add-shared-buffer.patch
Patch0375: 0375-Shared_buf-added-hypercall-for-shared_buf-setup.patch
Patch0376: 0376-ACRNTrace-add-acrn-trace-module.patch
Patch0377: 0377-sos-fix-potential-bugs-in-ptdev-msi-x-access.patch
Patch0378: 0378-vhm-cleanup-ioctls.patch
Patch0379: 0379-VHM-check-HV-api-version-for-VHM-module-init.patch
Patch0380: 0380-VHM-add-VHM-api-version-support.patch
Patch0381: 0381-virtio-framework-support-ACRN-virtio-devices.patch
Patch0382: 0382-VHM-sync-public-header-file-acrn_common.h.patch
Patch0383: 0383-Check-x86_hyper-type-before-doing-hypercall.patch
Patch0384: 0384-VHM-replace-function-name-update_mmio_map-with-updat.patch
Patch0385: 0385-VHM-refine-memory-segment-interface.patch
Patch0386: 0386-VBS-K-added-VHM-wrapper-APIs.patch
Patch0387: 0387-api-doc-add-ACRN-VBS-API-docs.patch
Patch0388: 0388-HVLog-reserve-memory-for-ACRN-HVLog.patch
Patch0389: 0389-HVLog-add-HVLog-module.patch
Patch0390: 0390-update-MEM_ATTR_WRITE_PROT-with-WB-policy.patch
Patch0391: 0391-vhm-modify-mmio-memory-map-unmap-api.patch
Patch0392: 0392-vhm-cleanup-update-one-field-name-in-vhm.patch
Patch0393: 0393-sos-add-a-config-for-VHM.patch
Patch0394: 0394-api-doc-add-vhm-API-docs.patch
Patch0395: 0395-api-doc-update-ACRN-VBS-API-docs.patch
Patch0396: 0396-license-update-intel-license-for-ACRN-VBS.patch
Patch0397: 0397-VBS-K-fix-compilation-warnings-in-VBS-K-reference-dr.patch
Patch0398: 0398-Cleanup-Kconfig.patch
Patch0399: 0399-skip-sbuf-and-vhm-initialization-when-booting-native.patch
Patch0400: 0400-VHM-add-hugetlb-page-ept-mapping-support.patch
Patch0401: 0401-VHM-change-VM_SYSMEM-VM_MMIO-to-VM_MEMMAP_SYSMEM-VM_.patch
Patch0402: 0402-VHM-add-hash-table-support-for-huge-pages.patch
Patch0403: 0403-VHM-add-service-to-support-px-data-transition.patch
Patch0404: 0404-sos-sync-common-header-file.patch
Patch0405: 0405-sos_kernel-export-restart-vm-function-to-DM.patch
Patch0406: 0406-VHM-add-service-to-support-cx-data-transition.patch
Patch0407: 0407-vhm-add-set_memmaps-hypercall-support.patch
Patch0408: 0408-vhm-use-set-memmaps-hypercall-for-hugetlb.patch
Patch0409: 0409-vhm-prepare-future-update-for-struct-vm_set_memmap.patch
Patch0410: 0410-VHM-bug-fix-on-operating-multi-thread-synchronizatio.patch
Patch0411: 0411-vhm-add-hypercall-to-set-sstate-data.patch
Patch0412: 0412-VHM-Update-cpu-id-type-as-uint16_t-for-struct-acrn_c.patch
Patch0413: 0413-vhm-add-sos-offline-cpu-support.patch
Patch0414: 0414-vhm-Fix-kernel-doc-issues.patch
Patch0415: 0415-vhm-add-trusty-init-de-init-support.patch
Patch0416: 0416-vhm-Rename-the-restart_vm-to-reset_vm.patch
Patch0417: 0417-vhm-fix-kerneldoc-format.patch
Patch0418: 0418-sos-vhm-remove-set-guest-memory-map-by-CMA.patch
Patch0419: 0419-sos-vhm-remove-hugetlb_enabled-flag.patch
Patch0420: 0420-sos-vhm-remove-MAP_MMIO.patch
Patch0421: 0421-vhm-revisit-types-in-structure-parameters-of-hyperca.patch
Patch0422: 0422-sos-vhm-add-hcall_write_protect_page-hypercall.patch
Patch0423: 0423-sos-vhm-refine-set-memory-region-API.patch
Patch0424: 0424-vhm-remove-re-schedule-for-ioreq-tasklet.patch
Patch0425: 0425-vhm-Add-vcpu_num-to-record-vcpu-number-of-each-VM.patch
Patch0426: 0426-vhm-mark-pending-ioreqs-in-bitmap-then-dispatch-it-t.patch
Patch0427: 0427-vhm-use-correct-string-length.patch
Patch0428: 0428-vhm-adapt-to-the-new-state-transition-of-VHM-request.patch
Patch0429: 0429-vhm-Add-error-handling-for-IC_CREATE_VM-ioctl.patch
Patch0430: 0430-vhm-setup-ioreq-shared-buf-in-IC_CREATE_VM-ioctl.patch
Patch0431: 0431-VBS-K-add-virtio_dev_reset.patch
Patch0432: 0432-VBS-K-Check-whether-vhm_client_id-is-valid-before-de.patch
Patch0433: 0433-VBS-K-add-reset-support-for-vbs_rng.patch
Patch0434: 0434-VBS-K-fix-a-bug-due-to-incorrect-check-of-return-val.patch
Patch0435: 0435-VHM-remove-panic-action-when-ioreq-fails.patch
Patch0436: 0436-vbs-fix-virtio_vq_index_get-func-handling-of-multi-V.patch
Patch0437: 0437-vhm-init-client-kthread_exit-true.patch
Patch0438: 0438-vhm-fix-client-use-after-free.patch
Patch0439: 0439-Adds-new-API-for-unmap-memseg.patch
Patch0440: 0440-sos-vhm-add-HC_SETUP_HV_NPK_LOG-hypercall.patch
Patch0441: 0441-acrn-add-hv_npk_log-module.patch
Patch0442: 0442-Adding-kernel-parameter-for-forcing-xapic-in-physica.patch
Patch0443: 0443-VHM-Add-EXPORT_SYMBOL-for-VHM-API-function-so-that-i.patch
Patch0444: 0444-vhm-deinit-trusty-after-hcall_destroy_vm.patch
Patch0445: 0445-VHM-add-ioctl-hypercall-for-UOS-intr-data-monitor.patch
Patch0446: 0446-vhm-enable-Werror-while-compiling-vhm-vbs-hyper-dmab.patch
Patch0447: 0447-vhm-change-trace_printk-of-vhm_dev_ioctl-to-pr_debug.patch
Patch0448: 0448-vhm-add-ioeventfd-support-for-ACRN-hypervisor-servic.patch
Patch0449: 0449-vhm-add-irqfd-support-for-ACRN-hypervisor-service-mo.patch
Patch0450: 0450-vhm-add-ioctl-for-set-clear-IRQ-line.patch
Patch0451: 0451-sos-vhm-add-hypercall-to-set-guest-vcpu-registers.patch
Patch0452: 0452-Kernel-VHM-Rename-acpi_generic_address-in-acrn_commo.patch
Patch0453: 0453-drm-i915-gvt-some-changes-to-support-xengt-acrngt.patch
Patch0454: 0454-drm-i915-gvt-Refactored-BXT-plane-registers.patch
Patch0455: 0455-drm-i915-gvt-passthru-PIPE_DSL-regiser-to-guest.patch
Patch0456: 0456-drm-i915-gvt-local-display-support.patch
Patch0457: 0457-drm-i915-gvt-local-display-support-in-GVT-g-guest.patch
Patch0458: 0458-drm-i915-gvt-Change-DomU-to-support-3-HDMI-displays.patch
Patch0459: 0459-drm-i915-i915-changes-to-allow-DomU-to-support-3-HDM.patch
Patch0460: 0460-drm-i915-gvt-removed-save-store-registers.patch
Patch0461: 0461-drm-i915-gvt-ivi-lazy-shadow-context.patch
Patch0462: 0462-drm-i915-gvt-add-some-MMIO-value-initialization.patch
Patch0463: 0463-drm-i915-gvt-added-option-to-disable-wa_ctx-shadowin.patch
Patch0464: 0464-drm-i915-gvt-enable-ppgtt-oos-sync-by-default.patch
Patch0465: 0465-drm-i915-gvt-emit-shadow-ppgtt-root-in-LRI.patch
Patch0466: 0466-drm-i915-gvt-Raise-a-uevent-when-Dom-0-is-ready-for-.patch
Patch0467: 0467-drm-i915-gvt-Don-t-load-CSR-for-Dom-U.patch
Patch0468: 0468-drm-i915-gvt-add-acrngt-support.patch
Patch0469: 0469-drm-i915-gvt-hard-code-Pipe-B-plane-owner-to-UOS.patch
Patch0470: 0470-drm-i915-gvt-remove-some-initialization-of-ggtt-in-G.patch
Patch0471: 0471-drm-i915-gvt-avoid-unncessary-reset-in-GVT-g-guest.patch
Patch0472: 0472-drm-i915-gvt-add-param-disable_gvt_fw_loading-to-dis.patch
Patch0473: 0473-drm-i915-gvt-inject-error-interrupt-to-DomU-when-GPU.patch
Patch0474: 0474-drm-i915-gvt-Added-error-interrupt-handler-for-GVT-g.patch
Patch0475: 0475-drm-i915-gvt-Add-the-support-of-HUC_STATUS2-reg-emul.patch
Patch0476: 0476-drm-i915-gvt-Add-vgt-id-in-context-id.patch
Patch0477: 0477-drm-i915-gvt-show-pid-hw_id-of-current-DomU-process-.patch
Patch0478: 0478-drm-i915-gvt-Add-new-trace-point-to-output-per-domai.patch
Patch0479: 0479-drm-i915-gvt-preliminary-per-ring-scheduler.patch
Patch0480: 0480-drm-i915-gvt-Support-vGPU-guest-framebuffer-GEM-obje.patch
Patch0481: 0481-drm-i915-gvt-unset-DDI_BUF_CTL_ENABLE-during-port-em.patch
Patch0482: 0482-drm-i915-gvt-add-scaler-owner-to-support-guest-plane.patch
Patch0483: 0483-drm-i915-gvt-support-guest-plane-scaling.patch
Patch0484: 0484-drm-i915-gvt-add-module-parameter-enable_pvmmio.patch
Patch0485: 0485-drm-i915-gvt-get-ready-of-memory-for-pvmmio.patch
Patch0486: 0486-drm-i915-implement-pvmmio-in-guest-i915.patch
Patch0487: 0487-drm-i915-gvt-implement-pvmmio-in-GVTg.patch
Patch0488: 0488-drm-i915-gvt-add-pvmmio-support-in-preempt-context-s.patch
Patch0489: 0489-drm-i915-Use-64-bit-write-to-optimize-writing-fence_.patch
Patch0490: 0490-drm-i915-gvt-don-t-treat-EINVAL-if-trap-pci_command-.patch
Patch0491: 0491-drm-i915-gvt-pvmmio-optimization-for-plane-update.patch
Patch0492: 0492-drm-i915-gvt-handling-pvmmio-update-of-plane-registe.patch
Patch0493: 0493-drm-i915-gvt-enable-plane-update-pvmmio-through-enab.patch
Patch0494: 0494-drm-i915-gvt-implement-gfn_to_mfn-with-identical-1-1.patch
Patch0495: 0495-drm-i915-gvt-cached-read_gpa-optimization-in-shadow-.patch
Patch0496: 0496-drm-i915-gvt-add-a-fastpath-for-cmd-parsing-on-MI_NO.patch
Patch0497: 0497-drm-i915-gvt-notify-ppgtt-update-through-g2v.patch
Patch0498: 0498-drm-i915-gvt-handle-ppgtt-update-from-g2v.patch
Patch0499: 0499-drm-i915-gvt-enable-pv-ppgtt-update-by-default.patch
Patch0500: 0500-drm-i915-gvt-pvmmio-optimization-for-plane-wm-regist.patch
Patch0501: 0501-drm-i915-gvt-handling-pvmmio-update-of-plane-wm-regi.patch
Patch0502: 0502-drm-i915-gvt-enable-plane-wm-pvmmio-level-through-en.patch
Patch0503: 0503-drm-i915-gvt-notify-global-gtt-update-through-g2v.patch
Patch0504: 0504-drm-i915-gvt-handle-global-gtt-update-from-g2v.patch
Patch0505: 0505-drm-i915-gvt-enable-pv-global-gtt-update-by-default.patch
Patch0506: 0506-drm-i915-gvt-Check-the-state-of-PVMMIO-gtt-table-to-.patch
Patch0507: 0507-drm-i915-gvt-allocate-ddb-according-to-active-pipes.patch
Patch0508: 0508-drm-i915-to-limit-the-supported-modifiers-for-plane-.patch
Patch0509: 0509-REVERTME-IOTG-hyper_dmabuf-Introducing-the-hyper_dma.patch
Patch0510: 0510-hyper_dmabuf-Enable-hyper_dmabuf-only-on-x86-or-x86_.patch
Patch0511: 0511-hyper_dmabuf-Fix-array-length-check-issue-in-hyper_d.patch
Patch0512: 0512-kernel-hyper_dmabuf-disable-hyper_dmabuf-on-arch-arm.patch
Patch0513: 0513-hyper_dmabuf-Remove-void-cast-in-cpu_access-function.patch
Patch0514: 0514-hyper_dmabuf-Fix-incorrect-return-in-hyper_dmabuf_op.patch
Patch0515: 0515-hyper_dmabuf-Check-for-NULL-value-before-access-work.patch
Patch0516: 0516-hyper_dmabuf-Remove-unused-variable-warnings.patch
Patch0517: 0517-hyper_dmabuf-virtio-Protect-virtqueue-operations-wit.patch
Patch0518: 0518-hyper_dmabuf-virtio-Correctly-cleanup-front-end-conn.patch
Patch0519: 0519-hyper_dmabuf-virtio-bugfix-on-acrn_ioreq_add_iorange.patch
Patch0520: 0520-hyper_dmabuf-virtio-Add-support-for-VBS_RESET_DEV-io.patch
Patch0521: 0521-hyper_dmabuf-virtio-Handle-S3-resume-correctly-v2.patch
Patch0522: 0522-hyper_dmabuf-fix-map-failure-issue-when-assign-4G-me.patch
Patch0523: 0523-hyper_dmabuf-fix-compile-warnings-in-hyper_dmabuf.patch
Patch0524: 0524-hyper_dmabuf-virtio-Adapt-to-the-new-state-transitio.patch
Patch0525: 0525-hyper_dmabuf-virtio-Process-ioreq-according-to-bitma.patch
Patch0526: 0526-hyper_dmabuf-virtio-Fixed-compilation-warnings.patch
Patch0527: 0527-hyper_dmabuf-Align-with-dma_buf_ops-changes.patch
Patch0528: 0528-drm-i915-diable-huge-page-ppgtt-when-using-PVMMIO-pp.patch
Patch0529: 0529-INTERNAL-IOTG-drm-i915-Decouple-pipe-and-crtc-index-.patch
Patch0530: 0530-INTERNAL-IOTG-drm-Don-t-assume-that-the-primary-plan.patch
Patch0531: 0531-INTERNAL-IOTG-drm-i915-Introduce-the-Plane-Restricti.patch
Patch0532: 0532-drm-i915-gvt-make-KBL-also-support-plane-restriction.patch
Patch0533: 0533-kernel-drm-i915-Check-the-plane_state-fb-to-avoid-Nu.patch
Patch0534: 0534-drm-i915-fix-a-kernel-panic-issue-of-plane-restricti.patch
Patch0535: 0535-drm-i915-gvt-ensure-each-pipe-has-a-plane-in-Host-OS.patch
Patch0536: 0536-drm-i915-to-limit-the-supported-modifiers-for-plane-.patch
Patch0537: 0537-drm-i915-Optimize-watermark-calculation-for-plane-re.patch
Patch0538: 0538-drm-i915-gvt-clean-up-the-cfg-space-and-MMIO-spaces.patch
Patch0539: 0539-drm-i915-gvt-use-plane-size-for-fb-decoder.patch
Patch0540: 0540-drm-i915-Sysfs-interface-to-get-GFX-shmem-usage-stat.patch
Patch0541: 0541-drm-i915-Async-work-for-hdcp-authentication.patch
Patch0542: 0542-drm-i915-Commit-CP-without-modeset.patch
Patch0543: 0543-MUST_REBASE-IOTG-drm-i915-Allow-late-GuC-HuC-loading.patch
Patch0544: 0544-drm-i915-Passing-the-intel_connector-to-HDCP-auth.patch
Patch0545: 0545-drm-Add-CP-downstream_info-property.patch
Patch0546: 0546-drm-Add-CP-System-Renewability-Msg-Property.patch
Patch0547: 0547-drm-i915-Add-HDCP-SRM-Blob-parsing.patch
Patch0548: 0548-drm-i915-Add-revocation-check-on-Ksvs.patch
Patch0549: 0549-drm-i915-Add-cp_downstream-property.patch
Patch0550: 0550-REVERTME-IOTG-drm-i915-Add-GuC-v9.29-and-HuC-v1.07-f.patch
Patch0551: 0551-test-configs-use-for-clean-and-android-bare-metal-BA.patch
#END XXXX: PK Series

# SEP and SoCWatch Series

# Clear Linux patch
# needs to add to PK series

%description
The Linux IOT LTS2018 kernel.

%package sos
License:        GPL-2.0
Summary:        The Linux kernel for Service OS
Group:          kernel

%description sos
The Linux kernel for Service OS

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel

%description extra
Linux kernel extra files

%prep
%setup -q -n linux-4.19-rc8

#patchXXXX PK Series
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1
%patch0024 -p1
%patch0025 -p1
%patch0026 -p1
%patch0027 -p1
%patch0028 -p1
%patch0029 -p1
%patch0030 -p1
%patch0031 -p1
%patch0032 -p1
%patch0033 -p1
%patch0034 -p1
%patch0035 -p1
%patch0036 -p1
%patch0037 -p1
%patch0038 -p1
%patch0039 -p1
%patch0040 -p1
%patch0041 -p1
%patch0042 -p1
%patch0043 -p1
%patch0044 -p1
%patch0045 -p1
%patch0046 -p1
%patch0047 -p1
%patch0048 -p1
%patch0049 -p1
%patch0050 -p1
%patch0051 -p1
%patch0052 -p1
%patch0053 -p1
%patch0054 -p1
%patch0055 -p1
%patch0056 -p1
%patch0057 -p1
%patch0058 -p1
%patch0059 -p1
%patch0060 -p1
%patch0061 -p1
%patch0062 -p1
%patch0063 -p1
%patch0064 -p1
%patch0065 -p1
%patch0066 -p1
%patch0067 -p1
%patch0068 -p1
%patch0069 -p1
%patch0070 -p1
%patch0071 -p1
%patch0072 -p1
%patch0073 -p1
%patch0074 -p1
%patch0075 -p1
%patch0076 -p1
%patch0077 -p1
%patch0078 -p1
%patch0079 -p1
%patch0080 -p1
%patch0081 -p1
%patch0082 -p1
%patch0083 -p1
%patch0084 -p1
%patch0085 -p1
%patch0086 -p1
%patch0087 -p1
%patch0088 -p1
%patch0089 -p1
%patch0090 -p1
%patch0091 -p1
%patch0092 -p1
%patch0093 -p1
%patch0094 -p1
%patch0095 -p1
%patch0096 -p1
%patch0097 -p1
%patch0098 -p1
%patch0099 -p1
%patch0100 -p1
%patch0101 -p1
%patch0102 -p1
%patch0103 -p1
%patch0104 -p1
%patch0105 -p1
%patch0106 -p1
%patch0107 -p1
%patch0108 -p1
%patch0109 -p1
%patch0110 -p1
%patch0111 -p1
%patch0112 -p1
%patch0113 -p1
%patch0114 -p1
%patch0115 -p1
%patch0116 -p1
%patch0117 -p1
%patch0118 -p1
%patch0119 -p1
%patch0120 -p1
%patch0121 -p1
%patch0122 -p1
%patch0123 -p1
%patch0124 -p1
%patch0125 -p1
%patch0126 -p1
%patch0127 -p1
%patch0128 -p1
%patch0129 -p1
%patch0130 -p1
%patch0131 -p1
%patch0132 -p1
%patch0133 -p1
%patch0134 -p1
%patch0135 -p1
%patch0136 -p1
%patch0137 -p1
%patch0138 -p1
%patch0139 -p1
%patch0140 -p1
%patch0141 -p1
%patch0142 -p1
%patch0143 -p1
%patch0144 -p1
%patch0145 -p1
%patch0146 -p1
%patch0147 -p1
%patch0148 -p1
%patch0149 -p1
%patch0150 -p1
%patch0151 -p1
%patch0152 -p1
%patch0153 -p1
%patch0154 -p1
%patch0155 -p1
%patch0156 -p1
%patch0157 -p1
%patch0158 -p1
%patch0159 -p1
%patch0160 -p1
%patch0161 -p1
%patch0162 -p1
%patch0163 -p1
%patch0164 -p1
%patch0165 -p1
%patch0166 -p1
%patch0167 -p1
%patch0168 -p1
%patch0169 -p1
%patch0170 -p1
%patch0171 -p1
%patch0172 -p1
%patch0173 -p1
%patch0174 -p1
%patch0175 -p1
%patch0176 -p1
%patch0177 -p1
%patch0178 -p1
%patch0179 -p1
%patch0180 -p1
%patch0181 -p1
%patch0182 -p1
%patch0183 -p1
%patch0184 -p1
%patch0185 -p1
%patch0186 -p1
%patch0187 -p1
%patch0188 -p1
%patch0189 -p1
%patch0190 -p1
%patch0191 -p1
%patch0192 -p1
%patch0193 -p1
%patch0194 -p1
%patch0195 -p1
%patch0196 -p1
%patch0197 -p1
%patch0198 -p1
%patch0199 -p1
%patch0200 -p1
%patch0201 -p1
%patch0202 -p1
%patch0203 -p1
%patch0204 -p1
%patch0205 -p1
%patch0206 -p1
%patch0207 -p1
%patch0208 -p1
%patch0209 -p1
%patch0210 -p1
%patch0211 -p1
%patch0212 -p1
%patch0213 -p1
%patch0214 -p1
%patch0215 -p1
%patch0216 -p1
%patch0217 -p1
%patch0218 -p1
%patch0219 -p1
%patch0220 -p1
%patch0221 -p1
%patch0222 -p1
%patch0223 -p1
%patch0224 -p1
%patch0225 -p1
%patch0226 -p1
%patch0227 -p1
%patch0228 -p1
%patch0229 -p1
%patch0230 -p1
%patch0231 -p1
%patch0232 -p1
%patch0233 -p1
%patch0234 -p1
%patch0235 -p1
%patch0236 -p1
%patch0237 -p1
%patch0238 -p1
%patch0239 -p1
%patch0240 -p1
%patch0241 -p1
%patch0242 -p1
%patch0243 -p1
%patch0244 -p1
%patch0245 -p1
%patch0246 -p1
%patch0247 -p1
%patch0248 -p1
%patch0249 -p1
%patch0250 -p1
%patch0251 -p1
%patch0252 -p1
%patch0253 -p1
%patch0254 -p1
%patch0255 -p1
%patch0256 -p1
%patch0257 -p1
%patch0258 -p1
%patch0259 -p1
%patch0260 -p1
%patch0261 -p1
%patch0262 -p1
%patch0263 -p1
%patch0264 -p1
%patch0265 -p1
%patch0266 -p1
%patch0267 -p1
%patch0268 -p1
%patch0269 -p1
%patch0270 -p1
%patch0271 -p1
%patch0272 -p1
%patch0273 -p1
%patch0274 -p1
%patch0275 -p1
%patch0276 -p1
%patch0277 -p1
%patch0278 -p1
%patch0279 -p1
%patch0280 -p1
%patch0281 -p1
%patch0282 -p1
%patch0283 -p1
%patch0284 -p1
%patch0285 -p1
%patch0286 -p1
%patch0287 -p1
%patch0288 -p1
%patch0289 -p1
%patch0290 -p1
%patch0291 -p1
%patch0292 -p1
%patch0293 -p1
%patch0294 -p1
%patch0295 -p1
%patch0296 -p1
%patch0297 -p1
%patch0298 -p1
%patch0299 -p1
%patch0300 -p1
%patch0301 -p1
%patch0302 -p1
%patch0303 -p1
%patch0304 -p1
%patch0305 -p1
%patch0306 -p1
%patch0307 -p1
%patch0308 -p1
%patch0309 -p1
%patch0310 -p1
%patch0311 -p1
%patch0312 -p1
%patch0313 -p1
%patch0314 -p1
%patch0315 -p1
%patch0316 -p1
%patch0317 -p1
%patch0318 -p1
%patch0319 -p1
%patch0320 -p1
%patch0321 -p1
%patch0322 -p1
%patch0323 -p1
%patch0324 -p1
%patch0325 -p1
%patch0326 -p1
%patch0327 -p1
%patch0328 -p1
%patch0329 -p1
%patch0330 -p1
%patch0331 -p1
%patch0332 -p1
%patch0333 -p1
%patch0334 -p1
%patch0335 -p1
%patch0336 -p1
%patch0337 -p1
%patch0338 -p1
%patch0339 -p1
%patch0340 -p1
%patch0341 -p1
%patch0342 -p1
%patch0343 -p1
%patch0344 -p1
%patch0345 -p1
%patch0346 -p1
%patch0347 -p1
%patch0348 -p1
%patch0349 -p1
%patch0350 -p1
%patch0351 -p1
%patch0352 -p1
%patch0353 -p1
%patch0354 -p1
%patch0355 -p1
%patch0356 -p1
%patch0357 -p1
%patch0358 -p1
%patch0359 -p1
%patch0360 -p1
%patch0361 -p1
%patch0362 -p1
%patch0363 -p1
%patch0364 -p1
%patch0365 -p1
%patch0366 -p1
%patch0367 -p1
%patch0368 -p1
%patch0369 -p1
%patch0370 -p1
%patch0371 -p1
%patch0372 -p1
%patch0373 -p1
%patch0374 -p1
%patch0375 -p1
%patch0376 -p1
%patch0377 -p1
%patch0378 -p1
%patch0379 -p1
%patch0380 -p1
%patch0381 -p1
%patch0382 -p1
%patch0383 -p1
%patch0384 -p1
%patch0385 -p1
%patch0386 -p1
%patch0387 -p1
%patch0388 -p1
%patch0389 -p1
%patch0390 -p1
%patch0391 -p1
%patch0392 -p1
%patch0393 -p1
%patch0394 -p1
%patch0395 -p1
%patch0396 -p1
%patch0397 -p1
%patch0398 -p1
%patch0399 -p1
%patch0400 -p1
%patch0401 -p1
%patch0402 -p1
%patch0403 -p1
%patch0404 -p1
%patch0405 -p1
%patch0406 -p1
%patch0407 -p1
%patch0408 -p1
%patch0409 -p1
%patch0410 -p1
%patch0411 -p1
%patch0412 -p1
%patch0413 -p1
%patch0414 -p1
%patch0415 -p1
%patch0416 -p1
%patch0417 -p1
%patch0418 -p1
%patch0419 -p1
%patch0420 -p1
%patch0421 -p1
%patch0422 -p1
%patch0423 -p1
%patch0424 -p1
%patch0425 -p1
%patch0426 -p1
%patch0427 -p1
%patch0428 -p1
%patch0429 -p1
%patch0430 -p1
%patch0431 -p1
%patch0432 -p1
%patch0433 -p1
%patch0434 -p1
%patch0435 -p1
%patch0436 -p1
%patch0437 -p1
%patch0438 -p1
%patch0439 -p1
%patch0440 -p1
%patch0441 -p1
%patch0442 -p1
%patch0443 -p1
%patch0444 -p1
%patch0445 -p1
%patch0446 -p1
%patch0447 -p1
%patch0448 -p1
%patch0449 -p1
%patch0450 -p1
%patch0451 -p1
%patch0452 -p1
%patch0453 -p1
%patch0454 -p1
%patch0455 -p1
%patch0456 -p1
%patch0457 -p1
%patch0458 -p1
%patch0459 -p1
%patch0460 -p1
%patch0461 -p1
%patch0462 -p1
%patch0463 -p1
%patch0464 -p1
%patch0465 -p1
%patch0466 -p1
%patch0467 -p1
%patch0468 -p1
%patch0469 -p1
%patch0470 -p1
%patch0471 -p1
%patch0472 -p1
%patch0473 -p1
%patch0474 -p1
%patch0475 -p1
%patch0476 -p1
%patch0477 -p1
%patch0478 -p1
%patch0479 -p1
%patch0480 -p1
%patch0481 -p1
%patch0482 -p1
%patch0483 -p1
%patch0484 -p1
%patch0485 -p1
%patch0486 -p1
%patch0487 -p1
%patch0488 -p1
%patch0489 -p1
%patch0490 -p1
%patch0491 -p1
%patch0492 -p1
%patch0493 -p1
%patch0494 -p1
%patch0495 -p1
%patch0496 -p1
%patch0497 -p1
%patch0498 -p1
%patch0499 -p1
%patch0500 -p1
%patch0501 -p1
%patch0502 -p1
%patch0503 -p1
%patch0504 -p1
%patch0505 -p1
%patch0506 -p1
%patch0507 -p1
%patch0508 -p1
%patch0509 -p1
%patch0510 -p1
%patch0511 -p1
%patch0512 -p1
%patch0513 -p1
%patch0514 -p1
%patch0515 -p1
%patch0516 -p1
%patch0517 -p1
%patch0518 -p1
%patch0519 -p1
%patch0520 -p1
%patch0521 -p1
%patch0522 -p1
%patch0523 -p1
%patch0524 -p1
%patch0525 -p1
%patch0526 -p1
%patch0527 -p1
%patch0528 -p1
%patch0529 -p1
%patch0530 -p1
%patch0531 -p1
%patch0532 -p1
%patch0533 -p1
%patch0534 -p1
%patch0535 -p1
%patch0536 -p1
%patch0537 -p1
%patch0538 -p1
%patch0539 -p1
%patch0540 -p1
%patch0541 -p1
%patch0542 -p1
%patch0543 -p1
%patch0544 -p1
%patch0545 -p1
%patch0546 -p1
%patch0547 -p1
%patch0548 -p1
%patch0549 -p1
%patch0550 -p1
%patch0551 -p1
# End XXXX PK Series

# SEP and SoCWatch Series

# Clear Linux patch

cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .
cp -a /usr/lib/firmware/i915 firmware/
cp -a /usr/lib/firmware/intel-ucode firmware/
cp -a /usr/lib/firmware/intel firmware/

%build
BuildKernel() {

    Target=$1
    Arch=x86_64
    ExtraVer="-%{release}.${Target}"

    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile

    make O=${Target} -s mrproper
    cp config-${Target} ${Target}/.config

    make O=${Target} -s ARCH=${Arch} olddefconfig
    make O=${Target} -s ARCH=${Arch} CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} %{?sparse_mflags}
}

BuildKernel %{ktarget0}
BuildKernel %{ktarget1}

%install

InstallKernel() {

    Target=$1
    Kversion=$2
    Arch=x86_64
    KernelDir=%{buildroot}/usr/lib/kernel

    mkdir   -p ${KernelDir}
    install -m 644 ${Target}/.config    ${KernelDir}/config-${Kversion}
    install -m 644 ${Target}/System.map ${KernelDir}/System.map-${Kversion}
    install -m 644 ${Target}/vmlinux    ${KernelDir}/vmlinux-${Kversion}
    install -m 644 cmdline-${Target}    ${KernelDir}/cmdline-${Kversion}
    cp  ${Target}/arch/x86/boot/bzImage ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}
    chmod 755 ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}

    mkdir -p %{buildroot}/usr/lib/modules
    make O=${Target} -s ARCH=${Arch} INSTALL_MOD_PATH=%{buildroot}/usr modules_install

    rm -f %{buildroot}/usr/lib/modules/${Kversion}/build
    rm -f %{buildroot}/usr/lib/modules/${Kversion}/source

    ln -s org.clearlinux.${Target}.%{version}-%{release} %{buildroot}/usr/lib/kernel/default-${Target}
}

InstallKernel %{ktarget0} %{kversion0}
InstallKernel %{ktarget1} %{kversion1}

rm -rf %{buildroot}/usr/lib/firmware

%files
%dir /usr/lib/kernel
%dir /usr/lib/modules/%{kversion0}
/usr/lib/kernel/config-%{kversion0}
/usr/lib/kernel/cmdline-%{kversion0}
/usr/lib/kernel/org.clearlinux.%{ktarget0}.%{version}-%{release}
/usr/lib/kernel/default-%{ktarget0}
/usr/lib/modules/%{kversion0}/kernel
/usr/lib/modules/%{kversion0}/modules.*

%files sos
%dir /usr/lib/kernel
%dir /usr/lib/modules/%{kversion1}
/usr/lib/kernel/config-%{kversion1}
/usr/lib/kernel/cmdline-%{kversion1}
/usr/lib/kernel/org.clearlinux.%{ktarget1}.%{version}-%{release}
/usr/lib/kernel/default-%{ktarget1}
/usr/lib/modules/%{kversion1}/kernel
/usr/lib/modules/%{kversion1}/modules.*

%files extra
%dir /usr/lib/kernel
/usr/lib/kernel/System.map-%{kversion0}
/usr/lib/kernel/System.map-%{kversion1}
/usr/lib/kernel/vmlinux-%{kversion0}
/usr/lib/kernel/vmlinux-%{kversion1}
