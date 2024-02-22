kpz = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1'
# Khởi tạo DataFrame trước vòng lặp
all_products = pd.DataFrame()

for i in range(1, 335):
    url2 = f"https://www.medigoapp.com/danh-muc/thuc-pham-chuc-nang?page={i}"
    response = requests.get(url2)
    hdr = {'User-Agent': kpz}
    req = Request(url2, headers=hdr)

    try:
        page = urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')
        grid_products_div = soup.find('div', class_='grid-products row m-0')

        # Kiểm tra xem có phần tử đó hay không
        if grid_products_div:
            # Ghi nội dung của phần tử vào DataFrame
            products = []

            for product_div in grid_products_div.find_all('div', class_='grid-products-item'):
                product = {}

                # Lấy thông tin từ thẻ hình ảnh
                image_tag = product_div.find('img', class_='post-thumb')
                if image_tag:
                    product['image'] = image_tag['src']

                # Lấy thông tin từ thẻ tiêu đề
                title_tag = product_div.find('h3', class_='line-clamp-3')
                if title_tag:
                    product['title'] = title_tag.text.strip()

                # Lấy thông tin giá và số lượng đã bán
                price_tag = product_div.find('p', class_='price')
                if price_tag:
                    product['price'] = price_tag.text.strip()

                sell_tag = product_div.find('p', class_='sell')
                if sell_tag:
                    product['sell'] = sell_tag.text.strip()

                products.append(product)

            # Chuyển danh sách sản phẩm thành DataFrame của pandas
            df = pd.DataFrame(products)

            # Thêm vào DataFrame chứa toàn bộ sản phẩm
            all_products = pd.concat([all_products, df], ignore_index=True)
            
            print(f"Đã xử lý trang {i}")
        else:
            print(f"Không tìm thấy phần tử có class='grid-products row m-0' trên trang {i}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Ghi toàn bộ DataFrame vào file CSV
csv_filename = 'products.csv'
all_products.to_csv(csv_filename, index=False, encoding='utf-8')

print(f'Thông tin đã được ghi vào file {csv_filename}')

