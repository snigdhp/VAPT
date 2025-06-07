# +RF Risk Faktörleri Hakkında Detaylar

## Top 10 Risk Faktörleri Özeti

Aşağıdaki tablo 2017 İlk 10 Uygulama Güvenliği Risklerini ve herbir risk için belirlediğimiz risk faktörlerinin bir özetini sunmaktadır. Bu faktörler hazır bulunan istatistik verilerine ve OWASP İlk 10 takımının tecrübelerine göre belirlenmiştir. Belirli bir uygulama veya kurum özelinde bu riskleri anlamak için, kendi tehdit etkenlerinizi ve iş etkilerinizi düşünmelisiniz. Gerekli saldırıyı gerçekleştirmek için bir tehdit etkeni bulunmuyorsa veya varlıklar için iş etkisi ihmal edilebilirse, ciddi yazılım açıklıkları bile ciddi bir risk oluşturmayabilmektedir.

![Risk Faktörleri Tablosu](images/0xc1-risk-factor-table.png)

## Düşünülmesi Gereken İlave Riskler

İlk 10 pek çok risk grubunu kapsamaktadır, ancak kurumunuzda düşünmeniz ve değerlendirmeniz gereken başka pek çok risk bulunmaktadır. Sürekli olarak keşfedilen yeni saldırı teknikleri dahil bunlardan bazıları daha önceki İlk 10 sürümlerinde belirtilmişken, bazıları ise belirtilmemiştir. Düşünmeniz gereken ilave diğer önemli uygulama güvenliği riskleri (CWE-ID değerlerine göre sıralı) aşağıdakileri içermektedir:

* [CWE-352: Siteler Arası İstek Sahteciliği (CSRF)](https://cwe.mitre.org/data/definitions/352.html)
* [CWE-400: Kontrolsüz Kaynak Tüketimi ('Kaynak Tüketimi', 'AppDoS')](https://cwe.mitre.org/data/definitions/400.html)
* [CWE-434: Sınırsız Dosya Yükleme](https://cwe.mitre.org/data/definitions/434.html)
* [CWE-451: Hassas Bilginin Kullanıcı Arayüzünde Yanlış Gösterimi (Clickjacking ve diğerleri)](https://cwe.mitre.org/data/definitions/451.html)
* [CWE-601: Doğrulanmamış Yönlendirme ve İletme](https://cwe.mitre.org/data/definitions/601.html)
* [CWE-799: Kontrolsüz Etkileşim Sıklığı (Anti-Otomasyon)](https://cwe.mitre.org/data/definitions/799.html)
* [CWE-829: Güvenilmeyen Fonksiyon Kullanımı (3. Parti İçerik)](https://cwe.mitre.org/data/definitions/829.html)
* [CWE-918: Sunucu Taraflı İstek Sahteciliği (SSRF)](https://cwe.mitre.org/data/definitions/918.html)

