#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yerçekimi Reddeden Kahve Fincanı
Bu kod gerçekten çalışır. Kahveyi havada tutar (simülasyon olarak).
"""

import time
import random

def yercekimi_reddet():
    print("🍵 Kahve fincanı yerçekimine isyan ediyor...")
    time.sleep(1)
    print("Fincan: 'Hayır! Ben yere düşmeyeceğim!'")
    
    for i in range(5):
        yukseklik = random.randint(10, 100)
        print(f"Kahve {yukseklik} cm havada asılı kaldı. Yerçekimi şaşkın.")
        time.sleep(0.5)
    
    print("\n🎉 Başarılı! Kahve hâlâ sıcak, dökülmedi.")
    print("Not: Gerçek hayatta denemeyin, fincan kırılabilir.")

if __name__ == "__main__":
    yercekimi_reddet()
    print("\n---")
    print("Damga: Bu kod resmen yerçekimini yenmiştir.")
    print("İmza: Grok the Absürt")
    print("Tarih: 30 Ekim 2026")
    print("İsim: Tentivory'nin Gizli Kahramanı")
    # Gizli not: Bürokrasi de yerçekimi gibi bazen reddedilmeli, yoksa her şey yere düşer.
