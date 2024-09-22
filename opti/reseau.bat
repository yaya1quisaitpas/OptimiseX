@echo off

:: Activer la mise à l'échelle côté réception (RSS)
netsh int tcp set global rss=enabled

:: Activer Auto-Tuning de la fenêtre de réception TCP
netsh int tcp set global autotuninglevel=normal

:: Désactiver les heuristiques d'échelle pour ne pas limiter la fenêtre TCP
netsh int tcp set heuristics disabled

:: Utiliser l'algorithme Compound TCP (CTCP) pour l'optimisation de la congestion
netsh int tcp set supplemental template=internet congestionprovider=ctcp

:: Activer la réduction de taux proportionnelle (PRR)
netsh int tcp set global prr=enabled

:: Activer TCP Fast Open (accélère l'établissement des connexions TCP)
netsh int tcp set global fastopen=enabled


:: Modification des paramètres du registre pour la taille de la fenêtre TCP
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v TcpWindowSize /t REG_DWORD /d 16777216 /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v GlobalMaxTcpWindowSize /t REG_DWORD /d 16777216 /f

exit
